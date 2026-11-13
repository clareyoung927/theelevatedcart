# Site build

The site is generated from these files. To change content, edit the data files, then run from the repo root:

    cd _build && python3 gen.py .. && cd ..

- data.py: tracking tag, recreated rooms (ROOMS), holiday rooms (HROOMS), short product names (P)
- guides.py: style guides (GUIDES)
- seo.py: quick answers and FAQs for each guide (required for every guide)
- gen.py: page templates, meta/Open Graph/Rich Pin tags, JSON-LD, sitemap.xml, robots.txt
- Local images live in /images (jpg, about 900px wide). Room photos load from Amazon's storefront CDN.

Folders starting with "_" are not published by GitHub Pages (Jekyll excludes them).
