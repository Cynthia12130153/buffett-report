"""Rebuild reports/index.json (newest first) from reports/YYYY-MM-DD.json."""
import json, pathlib
d = pathlib.Path(__file__).resolve().parent.parent / "reports"
ids = sorted((p.stem for p in d.glob("????-??-??.json")), reverse=True)
(d / "index.json").write_text(json.dumps(ids, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(ids)} reports indexed")
