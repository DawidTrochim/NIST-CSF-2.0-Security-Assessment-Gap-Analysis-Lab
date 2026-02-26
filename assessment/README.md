# NIST CSF 2.0 Audit & Gap Analysis Lab

A practical, GitHub-ready cybersecurity portfolio project that simulates a **NIST Cybersecurity Framework (CSF) 2.0** assessment for a fictional small-to-mid sized company.

This repository demonstrates how to:
- translate business context into a security assessment scope,
- map current controls to CSF outcomes,
- score maturity and risk consistently,
- produce a gap analysis and remediation backlog,
- communicate findings in a stakeholder-friendly report.

## Why this exists (portfolio value)
This project is intended for security practitioners who want a realistic artifact for interviews, consulting portfolios, and internal capability demonstrations. It includes both:
- **Executive-level outputs** (clear risk narrative, priorities, roadmap), and
- **Technical artifacts** (asset inventory, control matrix, evidence examples, scoring scripts).

All content is synthetic and safe for public sharing.

## Repository structure

```text
nist-csf-assessment/
├── README.md
├── control-mapping/
│   ├── csf_core_subset.md
│   ├── mapping_matrix.csv
│   └── scoring_criteria.md
├── sample-org-profile/
│   ├── org_overview.md
│   ├── asset_inventory.csv
│   ├── data_flows.md
│   ├── threat_model.md
│   └── assumptions.md
├── assessment/
│   ├── assessment-report.md
│   ├── current_profile.md
│   ├── target_profile.md
│   └── evidence/
│       ├── evidence_index.md
│       └── sample_evidence_artifacts.md
├── outputs/
│   ├── risk-register.csv
│   ├── gap-analysis.csv
│   └── remediation-backlog.csv
├── tools/
│   ├── scoring-model.py
│   ├── generate_outputs.py
│   └── requirements.txt
└── remediation-roadmap.md
```

## How to run locally

### 1) Clone and enter the project
```bash
git clone <your-fork-or-copy-url>
cd nist-csf-assessment
```

### 2) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
```

### 3) Install requirements
```bash
pip install -r tools/requirements.txt
```

### 4) Generate assessment outputs
```bash
python tools/generate_outputs.py
```

This command will:
- read the control mapping matrix and asset inventory,
- compute function-level maturity and overall maturity,
- produce updated `outputs/gap-analysis.csv` and `outputs/remediation-backlog.csv`,
- print a short summary of top gaps, highest risks, and quick wins.

## Screenshots (optional placeholders)
You can optionally include screenshots here when presenting this project:
- `docs/screenshots/assessment-summary.png` (placeholder)
- `docs/screenshots/top-gaps.png` (placeholder)
- `docs/screenshots/roadmap-view.png` (placeholder)

> No images are required to run this lab.

## How to extend this lab
- **Add outcomes**: extend `control-mapping/csf_core_subset.md` and `control-mapping/mapping_matrix.csv`.
- **Change organization profile**: edit `sample-org-profile/*` to simulate a different sector or threat landscape.
- **Tune scoring**: update formulas and weighting in `tools/scoring-model.py`.
- **Improve planning outputs**: refine prioritization and effort models in `outputs/` and scripts.

## Suggested usage pattern
1. Read the organization profile and assumptions.
2. Review data flows and threat model.
3. Walk through the control mapping and scoring criteria.
4. Read the assessment report and roadmap.
5. Re-run scripts to regenerate outputs and modify scenarios.

---

**Disclaimer:** This repository is a synthetic training and portfolio artifact, not legal or compliance advice.
