"""Inject library images into the template placeholders → dist/sheet-set.html
Only images present in library/ are embedded; the rest stay empty and can be
uploaded from the panel or supplied through a controlled project JSON."""
import base64, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE/"sheet-set.html").read_text()
KEYS = {"__LOGO__":"logo.png","__RENDER__":"render.jpg","__QR__":"qr.png","__AERIAL__":"aerial.png","__PARCEL__":"parcel.png",
        "__PLAN__":"plan.png","__TURNDOWN__":"turndown.png","__SLAB__":"slab.png","__PLATES__":"plates.png","__REBAR__":"rebar.png"}
def b64(p):
    mime = "image/jpeg" if p.suffix.lower() in (".jpg",".jpeg") else "image/png"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
for key,f in KEYS.items():
    p = HERE/"library"/f
    T = T.replace(key, b64(p) if p.exists() else "")
out = HERE/"dist"/"sheet-set.html"; out.parent.mkdir(exist_ok=True); out.write_text(T)
print("built", out, f"{len(T)/1024:.0f} kB")
