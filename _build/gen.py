import json, os, sys, html, shutil, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
from data import HROOMS, XMAS_LIST, TG_LIST, HAL_LIST, JULY4_LIST, BIG, UNAVAIL
from dupes import DUPES
import urllib.parse
from guides import GUIDES
from seo import GUIDE_SEO

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
SITE = "https://theelevatedcart.com"
NAME = "The Elevated Cart"
TODAY = datetime.date.today().isoformat()
PIN = "https://pin.it/2X4nS1eGx"
VERIFY = '<meta name="p:domain_verify" content="c5fe63e05fdcd9f3ea4e04e5fee37d6a"/>'
E = html.escape
X = 'target="_blank" rel="noopener sponsored nofollow"'

def plink(a): return f"https://www.amazon.com/dp/{a}?tag={TAG}"
def cartlink(a): return f"https://www.amazon.com/gp/aws/cart/add.html?ASIN.1={a}&Quantity.1=1&AssociateTag={TAG}"
def cartall(items):
    q = "&".join(f"ASIN.{i}={a}&Quantity.{i}=1" for i, (_, _, a) in enumerate(items, 1))
    return f"https://www.amazon.com/gp/aws/cart/add.html?{q}&AssociateTag={TAG}"
def buybar(shop, label, items):
    c = f'<a class="btn" href="{cartall(items)}" {X}>Add all to cart</a>' if items else ""
    return f'<div class="buybar"><a class="btn dark" href="{shop}" {X}>{label}</a>{c}</div>'
def items_of(asins): return [(P[a], plink(a), a) for a in asins if a not in UNAVAIL]

# alt text for local (non-room) images
LOCAL_ALT = {
 "entryway-drop-zone": "Entryway drop zone with a wood bench, shoes tucked underneath, wall hooks with coats and bags, and labeled woven baskets on a shelf above",
 "neutral-winter-mantel": "Neutral winter mantel with a large landscape painting, cream candlesticks, a rustic wood beam and a basket of firewood beside a white fireplace",
 "designer-christmas-tree": "Full Christmas tree with warm lights tucked deep inside, cream ribbon cascades and ornaments in three sizes beside a cozy armchair",
 "tree-base-styling": "Christmas tree base hidden by a large woven collar, with gifts wrapped in kraft paper and burgundy and green velvet ribbon",
 "cozy-christmas-bedroom": "Cozy Christmas bedroom with plaid pillows, a cream faux fur throw, a small wreath above the upholstered headboard and a lit mini tree",
 "christmas-eve-living-room": "Christmas Eve living room with a lit tree, knit stockings on the mantel, a glowing fire, plaid throw and mugs of cocoa on the coffee table",
 "christmas-breakfast-table": "Christmas morning breakfast table with pancakes and berries, plaid napkins, woven placemats, greenery and a hurricane candle",
 "coffee-cocoa-station": "Hot cocoa station on a marble counter with a wood tray, stoneware mugs, cinnamon sticks and jars of marshmallows",
 "christmas-pillows": "Stack of Christmas throw pillows on a window seat: a holly wreath pillow, a brown textured pillow, a red poinsettia pillow, a cream tartan plaid and a red plaid faux fur pillow",
 "thanksgiving-turkey-table": "Thanksgiving table set with green plaid linens, vintage turkey plates on woven chargers, a glass pumpkin dome with cookies, amber glasses and gold flatware",
 "july4-poolside-patio": "Poolside patio set for the Fourth of July with rattan chairs, navy star pillows, a red white and blue striped runner, stars plates and a pitcher of blue hydrangeas",
 "july4-americana-patio-table": "Outdoor wood dining table with a red white and blue stripe runner, woven placemats, Americana plates and white and blue hydrangeas, with an American flag behind",
 "july4-red-white-blue-tablescape": "Long outdoor teak table with a red striped linen tablecloth, red and white plates on woven placemats, hydrangeas and small flags beside a lit outdoor fireplace",
 "july4-americana-dinnerware": "Collage of stars and stripes dinnerware: patterned plates, a blue stars pitcher with hydrangeas, a woven tray and stacked blue bowls",
 "july4-americana-porch": "Covered porch set for the Fourth of July with an American flag, blue striped runner, patriotic pillows, lanterns, flag string lights and hydrangeas",
 "halloween-haunted-manor": "Halloween dining table with a cream runner printed with a black haunted mansion, black taper candles, bats and black dinner plates",
}

def room_alt(r):  # r = ROOMS tuple
    return f"{r[1].replace('The ', '', 1)} recreated with Amazon finds. {r[3]}"

def imginfo(ref):
    k, v = ref.split(":", 1)
    if k == "room":
        r = ROOMS[int(v)]; return CDN + r[4], room_alt(r)
    if k == "cdn": return CDN + v, None
    return f"/images/{v}.jpg", LOCAL_ALT.get(v, "")

# ---------- models ----------
rooms = []
for r in ROOMS:
    rooms.append(dict(slug=r[0], title=r[1], cat=r[2], blurb=r[3], img=CDN + r[4], alt=room_alt(r),
                      shop=PHOTO + r[5] + f"?tag={TAG}", items=items_of(r[6]),
                      url=f"/rooms/{r[0]}/", kind="room"))
roomby = {r["slug"]: r for r in rooms}
hrooms = []
for h in HROOMS:
    img, alt = imginfo(h[4])
    if h[6] is not None:
        base = ROOMS[h[6]]; items = items_of(base[6]); shop = PHOTO + base[5] + f"?tag={TAG}"; exact = True
    else:
        items = items_of(h[5]); shop = h[7]; exact = h[0] == "christmas-tablescape"
    if not alt: alt = f"{h[1].replace('The ', '', 1)}. {h[3]}"
    hrooms.append(dict(slug=h[0], title=h[1], hol=h[2], cat={'fourth': '4th of July'}.get(h[2], h[2].capitalize()), blurb=h[3], img=img, alt=alt,
                       items=items, shop=shop, exact=exact, url=f"/holiday/{h[0]}/", kind="hroom"))
guides = []
for g in GUIDES:
    img, alt = imginfo(g[4])
    guides.append(dict(slug=g[0], title=g[1], cat=g[2], hol=g[3], img=img, alt=alt, dek=g[5], body=g[6],
                       items=items_of(g[7]),
                       room=(roomby[ROOMS[g[8]][0]] if g[8] is not None else None),
                       url=f"/guides/{g[0]}/", kind="guide", seo=GUIDE_SEO[g[0]]))

dupes = []
for d in DUPES:
    o = dict(d); o.update(kind="dupe", url=f"/dupes/{d['slug']}/", img=f"/images/{d['img']}.jpg",
                          items=items_of([d["asin"]]), blurb=d["answer"])
    dupes.append(o)

# ---------- shared pieces ----------
css = open("base.css").read() + open("extra.css").read() + """
a.tile{color:inherit}
.crumbs{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-bottom:22px}
.crumbs a{text-decoration:none;color:var(--soft)}.crumbs a:hover{color:var(--ink)}
.answer{background:#FBF8F3;border:1px solid var(--line);border-left:3px solid var(--oak);padding:22px 24px;margin:28px 0}
.answer h2{font-size:22px!important;margin:0 0 8px!important}
.answer p{margin:0!important}
.item span.pthumb{display:block;background:var(--linen)}.item .pthumb{width:72px;height:72px;object-fit:contain;background:#fff;border:1px solid var(--line);flex:none;margin-right:14px}.item .iname{flex:1}
.buybar{display:flex;gap:10px;margin:0 0 18px}.buybar .btn{flex:1;text-align:center;padding:15px 8px;letter-spacing:.12em;white-space:nowrap}
.article.dupe{padding-top:22px}.dupe .crumbs{margin-bottom:10px}.dupe h1{font-size:clamp(26px,3vw,36px)!important;margin:4px 0 14px!important}.dupe .pinwrap{margin:0 0 12px}.dupe .disc{margin:0 0 16px;font-size:12px;padding:8px 12px}.dupe .shop{margin-top:0}.dupe .room-hero{max-height:calc(100vh - 310px);min-height:260px}
@media(max-width:700px){.article.dupe{padding-top:14px}.dupe .crumbs{display:none}.dupe h1{font-size:25px!important;margin:4px 0 12px!important}.dupe .room-hero{max-height:52vh}.buybar{position:sticky;bottom:0;z-index:5;background:var(--cream);padding:10px 0;margin:0 0 14px}}
.faq h3{font-family:"Cormorant Garamond",serif;font-weight:500;font-size:22px;margin:22px 0 6px}
.more{margin-top:56px}
.more h2{font-family:"Cormorant Garamond",serif;font-weight:400;font-size:32px;margin-bottom:22px}
.tile[hidden]{display:none}
.pinwrap{position:relative;margin:24px 0}.pinwrap .room-hero{margin:0}
.pinbtn{position:absolute;top:14px;right:14px;background:#E60023;color:#fff;text-decoration:none;font-size:13px;font-weight:500;letter-spacing:.04em;padding:9px 16px;border-radius:24px;box-shadow:0 2px 8px rgba(0,0,0,.18)}
.pinbtn:hover{background:#ad081b}
.item .acts{display:flex;gap:14px;flex-wrap:wrap;justify-content:flex-end}
.item a.cart{border-bottom:1px solid var(--olive);color:var(--olive)}
.cmp{width:100%;border-collapse:collapse;margin:20px 0 28px;font-size:15px}
.cmp th,.cmp td{text-align:left;padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.cmp th{font-family:Jost;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--soft);font-weight:500}
.cmp td:first-child{font-weight:500}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.legal{font-size:12px;color:var(--soft);margin-top:28px}
.links-page{max-width:520px;margin:0 auto;padding:40px 20px 60px;text-align:center}
.links-page .lbtn{display:block;padding:16px;margin:12px 0;border:1px solid var(--ink);text-decoration:none;font-size:13px;letter-spacing:.16em;text-transform:uppercase}
.links-page .lbtn.dark{background:var(--ink);color:var(--cream)}
.links-page .grid{grid-template-columns:1fr 1fr;gap:12px;text-align:left}
.links-page .tile-txt h3{font-size:19px}
@media(max-width:600px){.twocol{grid-template-columns:1fr}.cmp{font-size:14px}}
.pillars h3.pt{font-family:"Cormorant Garamond",serif;font-size:24px;font-weight:500;margin:0 0 6px}
"""

import hashlib
CSSV = hashlib.md5(css.encode()).hexdigest()[:8]
def head(title, desc, path, img, alt="", otype="website", ld=None):
    full = title if title.endswith(NAME) else f"{title} | {NAME}"
    imgabs = img if img.startswith("http") else SITE + img
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (ld or []))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{path}">
{VERIFY}
<meta property="og:site_name" content="{NAME}">
<meta property="og:type" content="{otype}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{E(imgabs)}">
<meta property="og:image:alt" content="{E(alt)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/images/mark.svg">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={CSSV}">
{lds}
</head>
<body>
<header><div class="wrap nav">
 <a class="brand" href="/"><img src="/images/mark.svg" alt="" width="46" height="46"><span>The Elevated Cart</span></a>
 <nav class="links" aria-label="Main">{{NAV}}</nav>
</div></header>
<main>
"""

def nav(active):
    items = [("rooms", "/rooms/", '<span class="f">Recreated </span>Rooms'), ("dupes", "/dupes/", '<span class="f">PB </span>Dupes'), ("guides", "/guides/", '<span class="f">Style </span>Guides'),
             ("holiday", "/holiday/", "Holiday"), ("about", "/about/", "About")]
    s = "".join(f'<a href="{u}" class="{"on" if k == active else ""}">{t}</a>' for k, u, t in items)
    return s + f'<a class="shop-tab" href="{STORE}" {X}>Shop</a>'

FOOT = f"""</main>
<footer><div class="wrap">
 <div class="foot">
  <div><a class="brand foot-brand" href="/"><img src="/images/mark.svg" alt="" width="52" height="52"><span>The Elevated Cart</span></a><p style="margin-top:14px;max-width:320px">Recreated rooms, styling guides and honest finds for a warm, layered home.</p></div>
  <nav aria-label="Site"><a href="/rooms/">Recreated Rooms</a><a href="/dupes/">Pottery Barn Dupes</a><a href="/guides/">Style Guides</a><a href="/holiday/">Holiday</a><a href="/about/">About</a><a href="/disclosure/">Affiliate Disclosure</a></nav>
  <nav aria-label="Social"><a href="{PIN}" target="_blank" rel="noopener">Pinterest</a><a href="https://www.instagram.com/theelevatedcart" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@theelevatedcart" target="_blank" rel="noopener">TikTok</a><a href="https://www.facebook.com/share/1FT9NSP1ji/" target="_blank" rel="noopener">Facebook</a><a href="{STORE}" {X}>Amazon Storefront</a></nav>
 </div>
 <div class="fine">As an Amazon Associate I earn from qualifying purchases. © 2026 The Elevated Cart</div>
</div></footer>
"""
FILTER_JS = """<script>
document.querySelectorAll('.chips').forEach(function(c){var g=document.getElementById(c.dataset.grid);
c.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;c.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});
var v=b.dataset.c;g.querySelectorAll('.tile').forEach(function(t){t.hidden=!(v==='All'||t.dataset.cat===v)})});
var h=(location.hash||'').slice(1);if(h){var b=c.querySelector('[data-c="'+h+'"]');if(b)b.click()}});
</script>"""

def page(path, active, title, desc, img, body, alt="", otype="website", ld=None, js=""):
    s = head(title, desc, path, img, alt, otype, ld).replace("{NAV}", nav(active)) + body + FOOT + js + "</body>\n</html>\n"
    sec = next((v for k, v in SECTION_TAGS.items() if path.startswith(k)), None)
    if sec:
        s = s.replace(STORE, "@@STORE@@").replace(f"tag={TAG}", f"tag={sec}").replace(f"AssociateTag={TAG}", f"AssociateTag={sec}").replace("@@STORE@@", STORE)
    p = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(s)
    PAGES.append(path)

PAGES = []
# Section tracking IDs: product, cart, shoppable-photo and list links on these pages use the section ID.
# Header/footer storefront links, the home page and /links/ keep the main website ID (TAG).
SECTION_TAGS = {"/rooms/": "theelevatedcartwebrooms-20", "/holiday/": "theelevatedcartwebholidays-20",
                "/dupes/": "theelevatedcartwebdupes-20", "/guides/": "theelevatedcartwebguides-20"}
def absimg(i): return i if i.startswith("http") else SITE + i
def hero(o):
    q = urllib.parse.urlencode({"url": SITE + o["url"], "media": absimg(o["img"]), "description": o["title"] + " | The Elevated Cart"})
    return (f'<figure class="pinwrap"><img class="room-hero" src="{E(o["img"])}" alt="{E(o["alt"])}">'
            f'<a class="pinbtn" href="https://www.pinterest.com/pin/create/button/?{E(q)}" target="_blank" rel="noopener" aria-label="Save to Pinterest">Save</a></figure>')
def label(o):
    return {"room": f"Recreated room · {o['cat']}", "hroom": f"Holiday · {o['cat']}", "guide": o["cat"], "dupe": f"Pottery Barn dupe · {o['cat']}"}[o["kind"]]
def tile(o, h="h3"):
    return f'<a class="tile" href="{o["url"]}" data-cat="{E(o["cat"])}"><img src="{E(o["img"])}" alt="{E(o["alt"])}" loading="lazy"><div class="tile-txt"><div class="eyebrow">{E(label(o))}</div><{h}>{E(o["title"])}</{h}></div></a>'
def grid(items, gid="", rooms_cls=True):
    return f'<div class="grid" id="{gid}">' + "".join(tile(o) for o in items) + "</div>"
def chips(cats, gid):
    return f'<div class="chips" data-grid="{gid}">' + "".join(f'<button class="chip {"on" if i == 0 else ""}" data-c="{c}">{c}</button>' for i, c in enumerate(cats)) + "</div>"
DISC = '<div class="disc">This post contains affiliate links. As an Amazon Associate I earn from qualifying purchases. <a href="/disclosure/">Learn more</a></div>'
try:
    AMZIMG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "amz_images.json")))["images"]
except Exception:
    AMZIMG = {}
def thumb(a):
    im = AMZIMG.get(a)
    return f'<img class="pthumb" src="{E(im["url"])}" alt="" loading="lazy">' if im else '<span class="pthumb"></span>'
def plist(items, head_, note):
    if not items: return ""
    return (f'<section class="shop" aria-labelledby="shoplist"><div class="eyebrow">Get the look</div><h2 id="shoplist" style="font-size:26px;margin:0 0 6px">{head_}</h2>'
            f'<p style="font-size:14px;color:var(--soft);margin-bottom:8px">{note}</p>'
            + "".join(f'<div class="item">{thumb(a)}<div class="iname"><b>{E(n)}</b></div><div class="acts"><a href="{u}" {X}>Shop on Amazon</a>' + '</div></div>' for n, u, a in items) + "</section>")
def crumbs(trail):
    html_ = " / ".join(f'<a href="{u}">{E(n)}</a>' if u else E(n) for n, u in trail)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + u} if u else {})} for i, (n, u) in enumerate(trail)]}
    return f'<nav class="crumbs" aria-label="Breadcrumb">{html_}</nav>', ld
def itemlist(name, items):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name,
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": it[0], "url": it[1]} for i, it in enumerate(items)]}
ORG = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE, "logo": SITE + "/images/mark.svg",
       "sameAs": ["https://www.instagram.com/theelevatedcart", "https://www.tiktok.com/@theelevatedcart"]}
AUTHOR = {"@type": "Organization", "name": NAME, "url": SITE}

# ---------- home ----------
H = {h["slug"]: h for h in hrooms}
home = f"""<div class="wrap"><div class="hero">
 <div><div class="eyebrow">Home styling, made simple</div>
 <h1>The designer look, <em>without</em> the designer price.</h1>
 <p>Designer rooms recreated with Amazon finds, plus styling guides for a warm, layered home. Every look is shoppable.</p>
 <div class="btns"><a class="btn dark" href="/rooms/">Shop the rooms</a><a class="btn" href="/guides/">Read the guides</a></div></div>
 <div class="hero-imgs"><img src="{E(rooms[0]['img'])}" alt="{E(rooms[0]['alt'])}"><img src="{E(rooms[9]['img'])}" alt="{E(rooms[9]['alt'])}"></div>
</div></div>
<section class="block"><div class="wrap"><div class="sec-head"><div><div class="eyebrow">The best part</div><h2>Recreated rooms</h2></div><a class="back" href="/rooms/">See all rooms →</a></div>{grid([rooms[0], rooms[1], rooms[5]])}</div></section>
<section class="block"><div class="wrap"><div class="sec-head"><div><div class="eyebrow">Look for less</div><h2>Pottery Barn dupes</h2></div><a class="back" href="/dupes/">See all dupes →</a></div>{grid(dupes[:3])}</div></section>
<section class="block holiday"><div class="wrap"><div class="sec-head"><div><div class="eyebrow">Holiday at home</div><h2>Holiday rooms</h2></div><a class="back" href="/holiday/">All holiday rooms →</a></div>{grid([H['christmas-tablescape'], H['christmas-pillows'], H['thanksgiving-turkey-table']])}</div></section>
<section class="block"><div class="wrap"><div class="sec-head"><div><div class="eyebrow">Style guides</div><h2>Style, simplified</h2></div><a class="back" href="/guides/">View all →</a></div>{grid([g for g in guides if not g['hol']][:3])}</div></section>
<section class="block promise"><div class="wrap">
 <div class="sec-head" style="justify-content:center;text-align:center"><div><div class="eyebrow">The Elevated Cart promise</div><h2>How every find is chosen</h2></div></div>
 <div class="pillars"><div><h3 class="pt">Looks like the inspiration</h3><p>Matched on shape, material and finish, not just category.</p></div>
 <div><h3 class="pt">Checked before it's shared</h3><p>Every product is a live listing, reviewed before it goes up.</p></div>
 <div><h3 class="pt">Styling first</h3><p>The how-to comes free. The shopping list is there if you want it.</p></div></div>
</div></section>"""
slugmap = {o["slug"]: o["url"] for o in rooms + guides}
slugmap.update({"holiday-" + h["slug"]: h["url"] for h in hrooms})
slugmap.update({k: f"/{k}/" for k in ["rooms", "guides", "holiday", "about", "disclosure"]})
redirect_js = f"""<script>(function(){{var m={json.dumps(slugmap)};var h=(location.hash||'').slice(1);if(m[h])location.replace(m[h]);}})();</script>"""
page("/", "", NAME, "Designer rooms recreated with Amazon finds, plus styling guides for a warm, layered home. Pottery Barn style looks without the designer price.",
     rooms[0]["img"], home, rooms[0]["alt"],
     ld=[ORG, {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE}], js=redirect_js)

# ---------- rooms ----------
body = f"""<div class="wrap" style="padding:56px 24px 72px"><div class="eyebrow">Recreated rooms</div>
<h1 class="vh">Designer rooms, recreated with Amazon finds</h1>
<p class="sub">Each room is fully shoppable. Tap a room to see the key pieces, or shop every item in the photo on my storefront.</p>
{chips(['All', 'Living Room', 'Dining', 'Bedroom'], 'g-rooms')}{grid(rooms, 'g-rooms')}
<div class="btns" style="margin-top:40px"><a class="btn dark" href="{ROOMS_STORE}" {X}>Shop all rooms on Amazon</a></div></div>"""
page("/rooms/", "rooms", "Recreated Rooms: Designer Looks with Amazon Finds", "Pottery Barn, Arhaus and Nancy Meyers inspired living rooms, dining rooms and bedrooms recreated with Amazon furniture and decor. Every piece is shoppable.",
     rooms[0]["img"], body, rooms[0]["alt"], ld=[itemlist("Recreated rooms", [(r["title"], SITE + r["url"]) for r in rooms])], js=FILTER_JS)

def related(pool, me, n=3):
    same = [o for o in pool if o is not me and o.get("cat") == me.get("cat")]
    other = [o for o in pool if o is not me and o not in same]
    return (same + other)[:n]

for r in rooms:
    cr, crld = crumbs([("Home", "/"), ("Recreated Rooms", "/rooms/"), (r["title"], None)])
    body = f"""<div class="wrap"><article class="article dupe">{cr}<h1>{E(r['title'])}</h1>
{hero(r)}{buybar(r['shop'], 'Shop this photo', r['items'])}{DISC}
{plist(r['items'], 'The key pieces', 'Each link is for the single item named.')}
<p class="dek">{E(r['blurb'])}</p>
<div class="more"><h2>More recreated rooms</h2>{grid(related(rooms, r))}</div></article></div>"""
    desc = f"{r['title'].replace('The ', '', 1)} recreated with Amazon finds: {r['blurb']} Shop every piece."
    page(r["url"], "rooms", r["title"] + " (Shop the Look)", desc[:300], r["img"], body, r["alt"], "article",
         ld=[crld, itemlist(r["title"] + " shopping list", r["items"]),
             {"@context": "https://schema.org", "@type": "Article", "headline": r["title"], "description": r["blurb"], "image": r["img"],
              "author": AUTHOR, "publisher": AUTHOR, "datePublished": "2026-11-13", "dateModified": TODAY, "mainEntityOfPage": SITE + r["url"]}])

# ---------- guides ----------
body = f"""<div class="wrap" style="padding:56px 24px 72px"><div class="eyebrow">Style guides</div>
<h1 class="vh">Style, simplified</h1>
<p class="sub">The how-to behind every look, with a shopping list at the end of each guide.</p>
{chips(['All', 'Living Room', 'Dining', 'Bedroom', 'Entryway', 'Holiday'], 'g-guides')}{grid(guides, 'g-guides')}</div>"""
page("/guides/", "guides", "Home Styling Guides: Measurements, Formulas and How-Tos", "Simple home styling guides: how high to hang art, what size rug you need, how to layer a bed, style a coffee table and decorate for the holidays.",
     guides[0]["img"], body, guides[0]["alt"], ld=[itemlist("Style guides", [(g["title"], SITE + g["url"]) for g in guides])], js=FILTER_JS)

for g in guides:
    q, a, faqs = g["seo"]
    cr, crld = crumbs([("Home", "/"), ("Style Guides", "/guides/"), (g["title"], None)])
    roombox = ""
    if g["room"] and not g["items"]:
        rr = g["room"]
        roombox = f'<section class="shop"><div class="eyebrow">Shop the photo</div><h2 style="font-size:26px;margin:0 0 6px">{E(rr["title"])}</h2><p style="font-size:14px;color:var(--soft);margin-bottom:14px">Every piece in this room is tagged on my Amazon storefront.</p><a class="btn dark" href="{rr["shop"]}" {X}>Shop the room</a> <a class="btn" href="{rr["url"]}">See the room</a></section>'
    elif not g["items"]:
        roombox = f'<section class="shop"><div class="eyebrow">Get the look</div><h2 style="font-size:26px;margin:0 0 6px">Shop my holiday picks</h2><p style="font-size:14px;color:var(--soft);margin-bottom:14px">Find my current favorites in my Amazon storefront.</p><a class="btn dark" href="{XMAS_LIST}" {X}>Shop on Amazon</a></section>'
    faqhtml = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{E(fq)}</h3><p>{E(fa)}</p>" for fq, fa in faqs) + "</section>"
    gbuy = buybar(g["room"]["shop"], "Shop this photo", g["items"]) if g["room"] else (buybar(STORE, "Shop on Amazon", g["items"]) if g["items"] else "")
    pool = [x for x in guides if bool(x["hol"]) == bool(g["hol"])]
    body = f"""<div class="wrap"><article class="article dupe">{cr}<h1>{E(g['title'])}</h1>
{hero(g)}{gbuy}{DISC}
{plist(g['items'], 'The shopping list', 'Each link is for the single item named. Styling props are not included unless listed.')}{roombox}
<p class="dek">{E(g['dek'])}</p>
<div class="answer"><h2>{E(q)}</h2><p>{E(a)}</p></div>
{g['body']}
{faqhtml}
<div class="more"><h2>More guides</h2>{grid(related(pool, g))}</div></article></div>"""
    page(g["url"], "guides", g["title"], f"{a}"[:300], g["img"], body, g["alt"], "article",
         ld=[crld, {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["dek"], "image": g["img"] if g["img"].startswith("http") else SITE + g["img"],
                    "author": AUTHOR, "publisher": AUTHOR, "datePublished": "2026-11-13", "dateModified": TODAY, "mainEntityOfPage": SITE + g["url"]},
             {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": fq, "acceptedAnswer": {"@type": "Answer", "text": fa}} for fq, fa in [(q, a)] + faqs]}]
            + ([itemlist(g["title"] + " shopping list", g["items"])] if g["items"] else []))

# ---------- holiday ----------
body = f"""<div class="wrap" style="padding:56px 24px 72px"><div class="eyebrow">Holiday at home</div>
<h1 class="vh">Holiday rooms, recreated with Amazon finds</h1>
<p class="sub">Every holiday look is shoppable. Tap a room to see the pieces. Looking for how-tos? <a href="/guides/#Holiday" style="color:var(--oak)">Jump to the holiday guides →</a></p>
{chips(['All', 'Christmas', 'Thanksgiving', 'Halloween', '4th of July'], 'g-hol')}{grid(hrooms, 'g-hol')}</div>"""
page("/holiday/", "holiday", "Holiday Rooms: Christmas, Thanksgiving, Halloween and 4th of July Looks", "Christmas tablescapes, Thanksgiving tables, holiday pillows, Halloween decor and Fourth of July patio looks recreated with Amazon finds. Shop every holiday look.",
     hrooms[0]["img"], body, hrooms[0]["alt"], ld=[itemlist("Holiday rooms", [(h["title"], SITE + h["url"]) for h in hrooms])], js=FILTER_JS)
LISTS = {"christmas": XMAS_LIST, "thanksgiving": TG_LIST, "halloween": HAL_LIST, "fourth": JULY4_LIST}
for h in hrooms:
    cr, crld = crumbs([("Home", "/"), ("Holiday", "/holiday/"), (h["title"], None)])
    lst = LISTS[h["hol"]]
    btn = f'<div class="btns" style="margin:0 0 8px"><a class="btn dark" href="{h["shop"]}" {X}>{"Shop every piece in this photo" if h["exact"] else "Shop the look on Amazon"}</a></div>' if h["shop"] else ""
    extra = f'<a class="btn" href="{lst}" {X}>Shop all {h["cat"]} decor</a>' if h["shop"] != lst else ""
    body = f"""<div class="wrap"><article class="article dupe">{cr}<h1>{E(h['title'])}</h1>
{hero(h)}{buybar(h['shop'] or lst, 'Shop this photo' if h['exact'] else 'Shop the look', h['items'])}{DISC}
{plist(h['items'], 'The key pieces', 'Each link is for the single item named.')}
<p class="dek">{E(h['blurb'])}</p>
<div class="btns"><a class="btn" href="/holiday/">More holiday rooms</a>{extra}</div>
<div class="more"><h2>More holiday rooms</h2>{grid(related(hrooms, h))}</div></article></div>"""
    page(h["url"], "holiday", h["title"] + " (Shop the Look)", f"{h['blurb']} Shop the {h['cat']} look with Amazon finds."[:300], h["img"], body, h["alt"], "article",
         ld=[crld, {"@context": "https://schema.org", "@type": "Article", "headline": h["title"], "description": h["blurb"], "image": h["img"] if h["img"].startswith("http") else SITE + h["img"],
                    "author": AUTHOR, "publisher": AUTHOR, "datePublished": "2026-11-13", "dateModified": TODAY, "mainEntityOfPage": SITE + h["url"]}]
            + ([itemlist(h["title"] + " shopping list", h["items"])] if h["items"] else []))

# ---------- dupes ----------
LEGAL = '<p class="legal">Pottery Barn is a trademark of its owner. The Elevated Cart is not affiliated with or endorsed by Pottery Barn. "Dupe" means a similar look at a lower price, not the same product. Pottery Barn prices are list prices noted on the date shown and may change.</p>'
body = f"""<div class="wrap" style="padding:56px 24px 72px"><div class="eyebrow">Look for less</div>
<h1 class="vh">Pottery Barn dupes on Amazon</h1>
<p class="sub">Pottery Barn pieces matched to Amazon look-alikes on shape, material and finish, with an honest side-by-side of what's the same and what's different.</p>
{chips(['All'] + sorted(set(d['cat'] for d in dupes)), 'g-dupes')}{grid(dupes, 'g-dupes')}{LEGAL}</div>"""
page("/dupes/", "dupes", "Pottery Barn Dupes on Amazon: Designer Look for Less", "Pottery Barn dupes on Amazon matched on shape, material and finish: floor mirrors, counter stools, dining chairs, bookcases and more, compared side by side.",
     dupes[0]["img"], body, dupes[0]["alt"], ld=[itemlist("Pottery Barn dupes", [(d["title"], SITE + d["url"]) for d in dupes])], js=FILTER_JS)
for d in dupes:
    cr, crld = crumbs([("Home", "/"), ("Pottery Barn Dupes", "/dupes/"), (d["title"], None)])
    pbp = f" ({d['pb_price']} as of {d['checked']})" if d["pb_price"] else ""
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in d["rows"])
    a0 = d["asin"]
    buy = f'<div class="buybar"><a class="btn dark" href="{plink(a0)}" {X}>View on Amazon</a><a class="btn" href="{cartlink(a0)}" {X}>Add to cart</a></div>'

    faqhtml = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q, a in d["faq"]) + "</section>"
    body = f"""<div class="wrap"><article class="article dupe">{cr}<h1>{E(d['title'])}</h1>
{hero(d)}{buy}{DISC}
{plist(d['items'], 'The Amazon find', "Amazon prices change often, so check today's price on the listing.")}
<p class="dek">The {E(d['pb'])}{E(pbp)} look, matched to an Amazon find.</p>
<div class="answer"><h2>What is the best {E(d['pb'])} dupe?</h2><p>{E(d['answer'])}</p></div>
<h2>Side by side</h2><table class="cmp"><thead><tr><th></th><th>{E(d['pb'].replace('Pottery Barn ', 'Pottery Barn '))}</th><th>Amazon find</th></tr></thead><tbody>{rows}</tbody></table>
<div class="twocol"><div><h2>What's the same</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in d['same'])}</ul></div><div><h2>What's different</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in d['diff'])}</ul></div></div>
<h2>How to style it</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in d['tips'])}</ul>
{faqhtml}{LEGAL}
<div class="more"><h2>More Pottery Barn dupes</h2>{grid(related(dupes, d))}</div></article></div>"""
    page(d["url"], "dupes", d["title"], d["answer"][:300], d["img"], body, d["alt"], "article",
         ld=[crld, {"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["answer"], "image": SITE + d["img"],
                    "author": AUTHOR, "publisher": AUTHOR, "datePublished": "2026-11-13", "dateModified": TODAY, "mainEntityOfPage": SITE + d["url"]},
             {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in [(f"What is the best {d['pb']} dupe?", d["answer"])] + d["faq"]]},
             itemlist(d["title"], d["items"])])

# ---------- links (bio link page) ----------
latest = [H['christmas-tablescape'], dupes[0], H['christmas-pillows'], rooms[-1], dupes[1], H['thanksgiving-turkey-table']]
body = f"""<div class="links-page"><img src="/images/mark.svg" alt="" width="84" height="84"><h1 class="serif" style="font-weight:400;font-size:32px;margin:10px 0 4px">The Elevated Cart</h1>
<p style="color:var(--soft);margin-bottom:18px">Designer looks, attainable finds. Tap any look to shop it.</p>
<a class="lbtn dark" href="{STORE}" {X}>Shop my Amazon storefront</a>
<a class="lbtn" href="/holiday/">Holiday rooms</a><a class="lbtn" href="/dupes/">Pottery Barn dupes</a><a class="lbtn" href="/rooms/">Recreated rooms</a>
<h2 class="serif" style="font-weight:400;font-size:26px;margin:28px 0 14px">Latest looks</h2>{grid(latest)}</div>"""
page("/links/", "", "The Elevated Cart Links", "Shop The Elevated Cart: latest recreated rooms, holiday looks, Pottery Barn dupes and my Amazon storefront.", rooms[0]["img"], body, rooms[0]["alt"])

# ---------- about / disclosure / 404 ----------
about = f"""<div class="wrap page" style="max-width:960px"><div class="about-grid"><div>
 <div class="eyebrow">About</div><h1>Hi, I'm Clare. Welcome to The Elevated Cart.</h1>
 <p>This is where the ideas from my Pinterest boards get the full story: the recreated rooms, the measurements, the layering order and the small details that make a room feel finished.</p>
 <p>I love the look of Pottery Barn, Arhaus and those warm, lived-in Nancy Meyers kitchens. I don't love paying for it. So I recreate those rooms with pieces that genuinely match the inspiration in shape, material and finish, and I only share ones I've checked.</p>
 <p>Every guide works without buying a thing. If you'd like the exact pieces, every room and guide links straight to them.</p>
 <p class="serif" style="font-size:24px;font-style:italic;color:var(--oak)">Thanks for being here.</p>
 <div class="btns"><a class="btn dark" href="/rooms/">Shop the rooms</a><a class="btn" href="/disclosure/">Affiliate disclosure</a></div>
</div><img src="/images/about.jpg" alt="Clare, founder of The Elevated Cart"></div></div>"""
page("/about/", "about", "About The Elevated Cart", "Designer-inspired rooms recreated with Amazon finds, chosen to match the inspiration in shape, material and finish.", "/images/about.jpg", about, "Clare, founder of The Elevated Cart")
disc = """<div class="wrap page"><div class="eyebrow">Disclosure</div><h1>Affiliate disclosure</h1>
 <p>The Elevated Cart is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</p>
 <p>As an Amazon Associate I earn from qualifying purchases. Links to Amazon on this site are affiliate links, which means I may earn a small commission if you buy through them, at no extra cost to you.</p>
 <p>Each shopping list names exactly what a link is for. Styling props in a photo are only included where they're listed. Prices and availability change, so please check the listing before you buy.</p>
 <p>Some images on this site are styled renderings created to show how pieces can work together in a room.</p></div>"""
page("/disclosure/", "", "Affiliate Disclosure", "The Elevated Cart affiliate disclosure for the Amazon Services LLC Associates Program.", rooms[0]["img"], disc, rooms[0]["alt"])
os.makedirs(OUT, exist_ok=True)
nf = head("Page not found", "This page could not be found.", "/404.html", rooms[0]["img"]).replace("{NAV}", nav("")) + \
     '<div class="wrap page"><h1>That page has moved.</h1><p>Try the <a href="/rooms/">recreated rooms</a>, the <a href="/guides/">style guides</a> or the <a href="/holiday/">holiday rooms</a>.</p></div>' + FOOT + "</body></html>"
open(os.path.join(OUT, "404.html"), "w").write(nf.replace('<link rel="canonical" href="https://theelevatedcart.com/404.html">', '<meta name="robots" content="noindex">'))

# ---------- assets, sitemap, robots ----------
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
open(os.path.join(OUT, "assets", "site.css"), "w").write(css)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in PAGES) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("pages", len(PAGES))
