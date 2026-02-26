# Scoring Criteria

## 1) Maturity scale (0-4)

| Score | Label | Definition |
|---|---|---|
| 0 | Absent | Control capability does not exist or is undocumented and unmanaged. |
| 1 | Ad-hoc | Activity is reactive, inconsistent, and heavily person-dependent. |
| 2 | Repeatable | Basic process exists and is reused, but coverage and quality are inconsistent. |
| 3 | Defined | Process is documented, approved, role-owned, and consistently executed. |
| 4 | Measured / Optimized | Outcomes are measured with KPIs/KRIs, tested regularly, and continuously improved. |

Interpretation guidance:
- 0-1 indicates urgent baseline risk.
- 2 indicates partial control reliability with known exposure.
- 3 indicates dependable operation suitable for most mid-market expectations.
- 4 indicates mature program-level capability.

## 2) Priority model (P1-P5)

Priority is derived using:

`Priority Driver Score = Impact x Likelihood x Exposure x Compliance Pressure`

Where each factor is scored 1-5:
- **Impact**: Business disruption, financial loss, customer trust impact.
- **Likelihood**: Probability of exploitation in current threat landscape.
- **Exposure**: Degree of internet exposure, privilege, data concentration, or weak control coverage.
- **Compliance Pressure**: Contractual/regulatory expectation from enterprise customers and auditors.

### Priority bands
| Priority | Driver score guidance | Meaning |
|---|---|---|
| P1 | 300-625 | Immediate action required; material risk to operations or key customer obligations. |
| P2 | 180-299 | High priority; schedule in next delivery window with executive oversight. |
| P3 | 90-179 | Medium priority; plan and track as part of quarterly uplift. |
| P4 | 40-89 | Lower priority; improve when dependency or efficiency opportunity appears. |
| P5 | 1-39 | Observe / accept with rationale; minimal near-term risk impact. |

## 3) Quick win definition

A control gap is a **Quick Win = Yes** when all conditions are met:
1. **Low implementation effort** (typically small policy/configuration/process change).
2. **High risk reduction** for one or more high-likelihood threats.
3. **Minimal dependencies** (no major procurement or architecture redesign).
4. **Deliverable in 30-60 days** with existing team capacity.

Examples of quick wins in this lab:
- Enforce MFA on remaining non-admin user groups.
- Formalize alert triage SLA and on-call escalation matrix.
- Standardize supplier security questionnaire for new vendors.

## 4) Scoring consistency rules
- Scoring must be evidence-led; no evidence defaults to maturity 0-1 unless justified.
- Maturity and status must align (e.g., "Implemented" should typically be maturity 3+).
- Where evidence conflicts, use the lower score and log follow-up evidence requests.
- Re-score after remediation to measure risk reduction over time.
