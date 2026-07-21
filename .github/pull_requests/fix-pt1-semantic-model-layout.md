---
title: chore(ProjectTest1): tidy PBIP semantic model layout and remove legacy placeholders
labels:
  - chores
  - infra
assignees: []
---

## Summary

Move semantic model TMDL files into the canonical `definition/tables/` folder and remove legacy placeholder PBIP folders under `ProjectTest1/PBIP`.

## Changes

- Moved `.tmdl` files into `ProjectTest1/PBIP/ProjectTest1.SemanticModel/definition/tables/`.
- Removed legacy placeholder directories: `ProjectTest1/PBIP/report/` and `ProjectTest1/PBIP/semantic/`.
- Updated project validation to pass (no behavior changes to report artifacts).

## Validation

- Ran `python ProjectTest1/tests/run_validation.py` — validator reports `PASS` (38 checks).

## Notes for reviewers

- This is a non-functional cleanup aligning the repository layout with the PBIP validator expectations.
- No changes to semantic model content or measures were made — files were relocated.

## How to test locally

```powershell
git fetch origin
git checkout -b fix/pt1/semantic-model-layout
git cherry-pick e773d2f
python ProjectTest1/tests/run_validation.py
```

If you want me to push the branch and open the PR I can do that (requires remote access).
