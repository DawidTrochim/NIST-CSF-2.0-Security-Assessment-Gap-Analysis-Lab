#!/usr/bin/env python3
"""Compute CSF maturity summaries and generate output planning CSV files."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
MAPPING_PATH = ROOT / "control-mapping" / "mapping_matrix.csv"
ASSET_PATH = ROOT / "sample-org-profile" / "asset_inventory.csv"
GAP_OUTPUT = ROOT / "outputs" / "gap-analysis.csv"
BACKLOG_OUTPUT = ROOT / "outputs" / "remediation-backlog.csv"

RISK_MULTIPLIER = {"Low": 1.0, "Med": 1.5, "High": 2.0}
STATUS_GAP_FACTOR = {
    "Implemented": 0.4,
    "Partial": 1.0,
    "Not Implemented": 1.4,
}
PRIORITY_TO_NUM = {"P1": 1, "P2": 2, "P3": 3, "P4": 4, "P5": 5}



def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))



def internet_exposure_factor(assets: List[Dict[str, str]]) -> float:
    if not assets:
        return 1.0
    exposed = sum(1 for a in assets if a.get("internet_exposed(Y/N)", "N").strip().upper() == "Y")
    ratio = exposed / len(assets)
    return round(1.0 + ratio, 2)



def function_maturity(mapping_rows: List[Dict[str, str]]) -> Dict[str, float]:
    bucket: Dict[str, List[float]] = defaultdict(list)
    for row in mapping_rows:
        try:
            bucket[row["function"]].append(float(row["maturity"]))
        except (ValueError, KeyError):
            continue

    return {
        func: round(sum(scores) / len(scores), 2)
        for func, scores in sorted(bucket.items())
        if scores
    }



def compute_gap_rows(mapping_rows: List[Dict[str, str]], exposure_factor: float) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for row in mapping_rows:
        status = row["implementation_status"]
        maturity = int(float(row["maturity"]))
        risk_label = row["risk_if_gap"]
        priority = row["priority"]
        quick_win = row.get("quick_win", "No")

        risk_score = round(
            RISK_MULTIPLIER.get(risk_label, 1.0)
            * STATUS_GAP_FACTOR.get(status, 1.0)
            * (5 - maturity)
            * exposure_factor,
            2,
        )

        effort = "S" if quick_win == "Yes" else ("L" if priority == "P1" else "M")
        dependencies = "None" if quick_win == "Yes" else "Cross-team coordination"
        recommended_action = f"Close gap for {row['outcome_title']} and validate evidence coverage"

        rows.append(
            {
                "outcome_id": row["outcome_id"],
                "function": row["function"],
                "status": status,
                "maturity": str(maturity),
                "risk_if_gap": risk_label,
                "recommended_action": recommended_action,
                "priority": priority,
                "effort(S/M/L)": effort,
                "dependencies": dependencies,
                "gap_risk_score": f"{risk_score:.2f}",
                "quick_win": quick_win,
            }
        )

    rows.sort(
        key=lambda r: (
            PRIORITY_TO_NUM.get(r["priority"], 99),
            -float(r["gap_risk_score"]),
            r["outcome_id"],
        )
    )
    return rows



def compute_backlog_rows(gap_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    backlog: List[Dict[str, str]] = []
    for idx, gap in enumerate(gap_rows, start=1):
        item_id = f"AUTO-{idx:03d}"
        target_quarter = "2026-Q2" if gap["priority"] in {"P1", "P2"} else "2026-Q3"
        backlog.append(
            {
                "item_id": item_id,
                "title": f"Remediate {gap['outcome_id']} ({gap['function']})",
                "description": gap["recommended_action"],
                "mapped_outcomes": gap["outcome_id"],
                "priority": gap["priority"],
                "effort(S/M/L)": gap["effort(S/M/L)"],
                "owner_role": function_owner(gap["function"]),
                "target_quarter": target_quarter,
                "success_criteria": f"Outcome {gap['outcome_id']} maturity increased and evidence logged",
                "notes": f"Auto-generated from gap risk score {gap['gap_risk_score']}",
            }
        )
    return backlog



def function_owner(function_name: str) -> str:
    return {
        "Govern": "CISO / Security Manager",
        "Identify": "Risk and Asset Management Lead",
        "Protect": "Infrastructure and Identity Lead",
        "Detect": "Security Operations Lead",
        "Respond": "Incident Response Manager",
        "Recover": "BCDR Coordinator",
    }.get(function_name, "Security Program Lead")



def write_csv(path: Path, fieldnames: List[str], rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)



def run() -> Dict[str, object]:
    mapping_rows = read_csv(MAPPING_PATH)
    assets = read_csv(ASSET_PATH)

    exposure_factor = internet_exposure_factor(assets)
    maturity_by_function = function_maturity(mapping_rows)
    overall_maturity = round(sum(maturity_by_function.values()) / len(maturity_by_function), 2)

    gap_rows = compute_gap_rows(mapping_rows, exposure_factor)
    backlog_rows = compute_backlog_rows(gap_rows)

    write_csv(
        GAP_OUTPUT,
        [
            "outcome_id",
            "function",
            "status",
            "maturity",
            "risk_if_gap",
            "recommended_action",
            "priority",
            "effort(S/M/L)",
            "dependencies",
            "gap_risk_score",
            "quick_win",
        ],
        gap_rows,
    )

    write_csv(
        BACKLOG_OUTPUT,
        [
            "item_id",
            "title",
            "description",
            "mapped_outcomes",
            "priority",
            "effort(S/M/L)",
            "owner_role",
            "target_quarter",
            "success_criteria",
            "notes",
        ],
        backlog_rows,
    )

    return {
        "maturity_by_function": maturity_by_function,
        "overall_maturity": overall_maturity,
        "gap_rows": gap_rows,
    }


if __name__ == "__main__":
    result = run()
    print("Generated outputs:")
    print(f"- {GAP_OUTPUT.relative_to(ROOT)}")
    print(f"- {BACKLOG_OUTPUT.relative_to(ROOT)}")
    print("Function maturity:")
    for fn, score in result["maturity_by_function"].items():
        print(f"  {fn}: {score}")
    print(f"Overall maturity: {result['overall_maturity']}")
