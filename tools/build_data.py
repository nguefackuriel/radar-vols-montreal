#!/usr/bin/env python3
"""Assemble data.json (lu par index.html) à partir d'un export de la base.

Usage : python3 tools/build_data.py <dossier_export> [sortie]
Le dossier d'export contient deals/*.json (vols), hotels/*.json (hôtels)
et meta/status.json.
"""
import json, pathlib, sys

def body(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, dict) and isinstance(d.get("data"), dict) and not ({"origin", "name", "lastRunAt"} & d.keys()):
        return d["data"]
    return d

FLIGHT = ("origin originCity dest destCity country region price usual saving pct airline stops "
          "duration depart ret url status foundAt lastSeenAt note source").split()
HOTEL = ("name city locality province provinceCode address stars rating reviews price usual saving pct "
         "checkin checkout nights url status foundAt lastSeenAt source note").split()

def main():
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "data.json")
    deals = [body(p) for p in sorted((src / "deals").glob("*.json"))]
    deals = [{k: d[k] for k in FLIGHT if k in d} for d in deals if d.get("origin") and d.get("dest")]
    hotels = [body(p) for p in sorted((src / "hotels").glob("*.json"))]
    hotels = [{k: h[k] for k in HOTEL if k in h} for h in hotels if h.get("name") and h.get("city")]
    meta_file = src / "meta" / "status.json"
    meta = body(meta_file) if meta_file.exists() else {}
    meta["dealsActive"] = sum(1 for d in deals if d.get("status") != "expired")
    meta["hotelsActive"] = sum(1 for h in hotels if h.get("status") == "active")
    out.write_text(json.dumps({"meta": meta, "deals": deals, "hotels": hotels}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out}: {len(deals)} vols ({meta['dealsActive']} actifs), {len(hotels)} hôtels ({meta['hotelsActive']} actifs)")

if __name__ == "__main__":
    main()
