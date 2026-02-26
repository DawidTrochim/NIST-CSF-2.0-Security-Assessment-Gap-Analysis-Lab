# NIST CSF 2.0 Audit & Gap Analysis Lab

A portfolio-grade security assessment project that simulates a full
**NIST Cybersecurity Framework (CSF) 2.0** control maturity and gap
analysis for a fictional small-to-mid sized organization.

This lab demonstrates how to translate business context into a
structured security assessment, score maturity consistently, quantify
risk exposure, and generate a prioritized remediation roadmap.

All content is synthetic and safe for public sharing.

------------------------------------------------------------------------

# Project Objective

This project answers a practical question:

How do you turn a control framework like NIST CSF into measurable,
risk-based, actionable outputs?

Instead of producing only a static PDF, this lab:

-   Maps organizational controls to CSF 2.0 outcomes
-   Scores maturity per function
-   Calculates weighted gap risk
-   Generates a structured gap analysis
-   Produces a prioritized remediation backlog
-   Outputs executive-friendly summaries

It simulates how a consultant or internal security lead would assess and
improve a growing organization's cybersecurity posture.

------------------------------------------------------------------------

# Scenario Overview

**Fictional Company: Northbridge Supplies Ltd**

-   Sector: UK-based B2B logistics and warehousing
-   Size: \~180 staff, two sites plus remote workforce
-   Tech stack: Microsoft 365, Entra ID, Windows endpoints, small
    on-prem VM cluster, Azure-hosted customer portal
-   Business priorities: uptime, customer portal availability,
    enterprise client trust

The organization has implemented some security controls but lacks
structured governance, mature detection capability, and formalized risk
tracking.

This assessment evaluates the current posture and defines a realistic
improvement roadmap.

------------------------------------------------------------------------

# What This Project Actually Does

The included scoring engine:

1.  Reads the control mapping matrix
2.  Evaluates implementation status and maturity
3.  Computes function-level maturity scores
4.  Calculates weighted risk for control gaps
5.  Identifies high-priority and high-impact weaknesses
6.  Generates:
    -   Gap analysis report (CSV)
    -   Remediation backlog (CSV)
    -   Function maturity summary
    -   Overall maturity score

Example output:

Function maturity: Detect: 1.4 Govern: 1.8 Identify: 1.8 Protect: 2.14
Recover: 1.5 Respond: 1.6

Overall maturity: 1.71

This indicates an organization operating between ad-hoc and repeatable
maturity levels, with detection capability being the weakest domain.

------------------------------------------------------------------------

# Repository Structure

nist-csf-assessment/ ├── README.md ├── control-mapping/ ├──
sample-org-profile/ ├── assessment/ ├── outputs/ ├── tools/ └──
remediation-roadmap.md

------------------------------------------------------------------------

# How to Run Locally

1.  Clone the repository

git clone `<your-repo-url>`{=html} cd nist-csf-assessment

2.  Create virtual environment

Windows: python -m venv .venv .venv`\Scripts`{=tex}`\activate`{=tex}

Linux/macOS: python3 -m venv .venv source .venv/bin/activate

3.  Install requirements

pip install -r tools/requirements.txt

4.  Generate outputs

python tools/generate_outputs.py

This will: - Calculate function-level maturity - Compute overall
maturity - Generate gap-analysis.csv - Generate
remediation-backlog.csv - Print top risks and quick wins

------------------------------------------------------------------------

# What the Outputs Represent

## Function Maturity

Average maturity per CSF Function:

-   Govern
-   Identify
-   Protect
-   Detect
-   Respond
-   Recover

Scale:

0 = nonexistent 1 = ad-hoc 2 = repeatable 3 = defined 4 = measured and
optimized

------------------------------------------------------------------------

## Gap Analysis

Structured list of: - Outcome ID - Implementation status - Risk level -
Recommended action - Priority - Effort estimate

------------------------------------------------------------------------

## Remediation Backlog

Actionable roadmap items including: - Title - Priority - Effort
estimate - Target quarter - Success criteria

------------------------------------------------------------------------

# Key Skills Demonstrated

-   NIST CSF 2.0 control mapping
-   Security maturity modeling
-   Risk-based prioritization
-   Control gap quantification
-   Governance and risk awareness
-   Structured remediation planning
-   Technical scripting for audit automation
-   Executive and technical report writing

------------------------------------------------------------------------

# Why This Is Different

Many audit projects are static documents.

This lab: - Automates scoring - Generates dynamic outputs - Allows
scenario modification - Simulates consultancy workflows - Produces
reproducible results

------------------------------------------------------------------------

# Disclaimer

This repository is a synthetic training and portfolio artifact. It does
not constitute legal, compliance, or regulatory advice.
