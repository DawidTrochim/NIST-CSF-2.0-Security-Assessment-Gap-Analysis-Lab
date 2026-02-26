#!/usr/bin/env python3
"""Regenerate outputs and print an assessor-friendly summary."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORING_SCRIPT = ROOT / "tools" / "scoring-model.py"
GAP_OUTPUT = ROOT / "outputs" / "gap-analysis.csv"


def read_csv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    completed = subprocess.run([sys.executable, str(SCORING_SCRIPT)], cwd=ROOT, check=False)
    if completed.returncode != 0:
        print("Failed to generate outputs from scoring model.")
        return completed.returncode

    gap_rows = read_csv(GAP_OUTPUT)

    top_gaps = [r for r in gap_rows if r["priority"] == "P1"][:5]
    high_risks = sorted(gap_rows, key=lambda r: float(r["gap_risk_score"]), reverse=True)[:5]
    quick_wins = [r for r in gap_rows if r.get("quick_win") == "Yes"][:5]

    print("\n=== Assessment Output Summary ===")
    print("Top P1 gaps:")
    for row in top_gaps:
        print(f"- {row['outcome_id']} ({row['function']}): {row['status']} | risk={row['risk_if_gap']}")

    print("\nHighest computed gap risks:")
    for row in high_risks:
        print(
            f"- {row['outcome_id']} score={row['gap_risk_score']} "
            f"priority={row['priority']} status={row['status']}"
        )

    print("\nQuick wins:")
    for row in quick_wins:
        print(f"- {row['outcome_id']} ({row['function']}) priority={row['priority']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
