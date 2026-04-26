#!/usr/bin/env python3
"""
Import Anthropic's skill-creator files into this repository.

Usage from repo root:
  python Skills/skill-creator/import_skill_creator.py

This downloads the upstream files from:
  https://github.com/anthropics/skills/tree/main/skills/skill-creator

License:
  Upstream files are Apache-2.0. Keep LICENSE.txt with the imported folder.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlopen, Request

ROOT = Path(__file__).resolve().parents[2]
TARGET_ROOT = ROOT / "Skills" / "skill-creator"
RAW_BASE = "https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator"

FILES = [
    "SKILL.md",
    "LICENSE.txt",
    "agents/grader.md",
    "agents/analyzer.md",
    "agents/comparator.md",
    "assets/eval_review.html",
    "eval-viewer/generate_review.py",
    "eval-viewer/viewer.html",
    "references/schemas.md",
    "scripts/aggregate_benchmark.py",
    "scripts/generate_report.py",
    "scripts/improve_description.py",
    "scripts/package_skill.py",
    "scripts/quick_validate.py",
    "scripts/run_eval.py",
    "scripts/run_loop.py",
    "scripts/utils.py",
]


def download_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "project-agent-skill-importer"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def main() -> None:
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    for rel_path in FILES:
        url = f"{RAW_BASE}/{rel_path}"
        output_path = TARGET_ROOT / rel_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloading {rel_path}...")
        output_path.write_text(download_text(url), encoding="utf-8")
    print(f"Done. Imported {len(FILES)} files into {TARGET_ROOT}")


if __name__ == "__main__":
    main()
