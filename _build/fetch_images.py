"""Daily: pull product images from Amazon Creators API into amz_images.json.
Runs in GitHub Actions with secrets AMZ_CLIENT_ID and AMZ_CLIENT_SECRET.
Images are Amazon-hosted URLs returned by the API (never downloaded or re-hosted)."""
import json, os, sys, urllib.request, datetime, time
sys.path.insert(0, os.path.dirname(__file__))
from data import P, UNAVAIL
from dupes import DUPES
TAG = "theelevatedcartweb-20"
cid, sec = os.environ.get("AMZ_CLIENT_ID"), os.environ.get("AMZ_CLIENT_SECRET")
if not cid or not sec:
    sys.exit("Missing AMZ_CLIENT_ID / AMZ_CLIENT_SECRET")
def post(url, body, headers):
    req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())
tok = post("https://api.amazon.com/auth/o2/token", {"grant_type": "client_credentials", "client_id": cid,
          "client_secret": sec, "scope": "creatorsapi::default"}, {})["access_token"]
asins = sorted(set(list(P)) | {d["asin"] for d in DUPES})
asins = [a for a in asins if a not in UNAVAIL]
out, errs = {}, []
err = ''
batches = [asins[i:i + 10] for i in range(0, len(asins), 10)]
def run(batches):
  for chunk in batches:
    _one(chunk)
def _one(chunk):
    global err
    r = None
    for attempt in range(5):
        time.sleep(1.5 * (attempt + 1))
        try:
            r = post("https://creatorsapi.amazon/catalog/v1/getItems",
                     {"itemIds": chunk, "itemIdType": "ASIN", "marketplace": "www.amazon.com", "partnerTag": TAG,
                      "partnerType": "Associates", "resources": ["images.primary.large"]},
                     {"Authorization": "Bearer " + tok, "x-marketplace": "www.amazon.com"})
            break
        except Exception as e:
            err = f"{chunk[0]}: {e}"
    if r is None:
        errs.append(err); return
    items = (r.get("itemsResult") or r.get("ItemsResult") or {}).get("items") or (r.get("ItemsResult") or {}).get("Items") or []
    for it in items:
        a = it.get("asin") or it.get("ASIN")
        im = (it.get("images") or it.get("Images") or {}).get("primary") or (it.get("Images") or {}).get("Primary") or {}
        m = im.get("large") or im.get("Large") or im.get("medium") or {}
        u = m.get("url") or m.get("URL")
        if a and u:
            out[a] = {"url": u, "w": m.get("width") or m.get("Width"), "h": m.get("height") or m.get("Height")}
run(batches)
missing = [a for a in asins if a not in out]
if missing:
    print(f"retrying {len(missing)} one by one")
    run([[a] for a in missing])
here = os.path.dirname(os.path.abspath(__file__))
json.dump({"fetched": datetime.datetime.utcnow().isoformat(timespec="minutes") + "Z", "images": out},
          open(os.path.join(here, "amz_images.json"), "w"), indent=0, sort_keys=True)
print(f"{len(out)}/{len(asins)} images; {len(errs)} errors")
for e in errs[:5]: print(e)
if not out: sys.exit(1)
