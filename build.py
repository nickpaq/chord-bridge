from pathlib import Path

root = Path(__file__).resolve().parent
(root / "Chord Bridge.html").write_text(
    (root / "page.html").read_text().replace("/* CORE */", (root / "core.js").read_text())
)
