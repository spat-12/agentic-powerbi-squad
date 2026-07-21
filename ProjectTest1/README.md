# ProjectTest1

This folder contains a starter Power BI project scaffold for `ProjectTest1`.

Structure:
- `spec/` — project specification (starter)
- `data/` — generated CSV mock data
- `scripts/generate_data.py` — data generator (writes into `data/`)
- `PBIP/semantic/` — placeholder TMDL files
- `PBIP/report/` — placeholder PBIR pages
- `tests/run_validation.py` — simple validation runner used by CI

Quick start (local):

```bash
python ProjectTest1/scripts/generate_data.py
python ProjectTest1/tests/run_validation.py
```

Expand the spec, TMDL, and PBIR files to implement the full project.
