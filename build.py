from pathlib import Path

root = Path(__file__).resolve().parent
html = (root / "page.html").read_text(encoding="utf-8").replace(
    "/* CORE */", (root / "core.js").read_text(encoding="utf-8")
)
for name in ("Chord Bridge.html", "index.html"):
    (root / name).write_text(html, encoding="utf-8")
