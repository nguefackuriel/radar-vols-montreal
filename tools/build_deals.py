#!/usr/bin/env python3
"""Assemble deals.json (lu par index.html) à partir d'un export de la base.

Usage : python3 tools/build_deals.py <dossier_export> [sortie]
Le dossier d'export contient deals/*.json (une fiche par aubaine) et,
si présent, meta/status.json (lastRunAt, routesScanned, dealsActive).
"""
import json, pathlib, sys

def body(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    return d["data"] if isinstance(d, dict) and isinstance(d.get("data"), dict) and "origin" not in d and "lastRunAt" not in d else d

def main():
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "deals.json")
    deals = [body(p) for p in sorted((src / "deals").glob("*.json"))]
    keep = ("origin originCity dest destCity country region price usual saving pct airline stops "
            "duration depart ret url status foundAt lastSeenAt note source").split()
    deals = [{k: d[k] for k in keep if k in d} for d in deals if d.get("origin") and d.get("dest")]
    meta_file = src / "meta" / "status.json"
    meta = body(meta_file) if meta_file.exists() else {}
    meta["dealsActive"] = sum(1 for d in deals if d.get("status") != "expired")
    out.write_text(json.dumps({"meta": meta, "deals": deals}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out}: {len(deals)} aubaines, {meta['dealsActive']} actives")

if __name__ == "__main__":
    main()
