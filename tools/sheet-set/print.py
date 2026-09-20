"""Print dist/sheet-set.html (optionally with a project JSON applied) to a 36×24 PDF.
usage: python print.py [project.json] [out.pdf]     requires: pip install playwright && playwright install chromium"""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
html = (HERE/"dist"/"sheet-set.html").resolve()
proj = pathlib.Path(sys.argv[1]).read_text() if len(sys.argv) > 1 and sys.argv[1] else None
out = sys.argv[2] if len(sys.argv) > 2 else "sheet-set.pdf"
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width":1800,"height":1200})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(html.as_uri()); pg.wait_for_timeout(800)
    if proj:
        pg.evaluate("st => { Object.assign(PROJECT, st.project||st); if(st.images) Object.assign(IMG, st.images); fill(); render(); }", json.loads(proj))
        pg.wait_for_timeout(300)
    ov = pg.evaluate("()=>[...document.querySelectorAll('.block,.slot,.notes,.stub,.seq .step,.disclaim,.takeoff,.tb')].filter(e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2).map(e=>e.className)")
    pg.emulate_media(media="print")
    pg.pdf(path=out, width="36in", height="24in", print_background=True, prefer_css_page_size=True)
    b.close()
print("pdf:", out, "| js errors:", errs, "| overflow:", ov)
