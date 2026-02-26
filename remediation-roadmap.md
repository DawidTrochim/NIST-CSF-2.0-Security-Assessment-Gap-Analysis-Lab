# Remediation Roadmap (Practical, Prioritized)

## Planning principles
- Prioritize reductions in ransomware, credential abuse, and portal compromise risk.
- Balance rapid wins with foundational process improvements.
- Tie every initiative to measurable outcomes and CSF subset IDs.

## Phase 0-30 days (Stabilize high-risk exposure)

| Initiative | CSF Mapping | Priority | Measurable Outcome |
|---|---|---|---|
| 1. Complete MFA enforcement for remaining users | PR-2, PR-1 | P1 | MFA coverage reaches >98% of active users. |
| 2. Publish top 10 SIEM detections for core threats | DE-2, DE-1 | P1 | Detection catalog approved; alerts generating tickets. |
| 3. Establish supplier security intake checklist | GV-5 | P1 | 100% new critical suppliers assessed before onboarding. |
| 4. Approve incident communications templates | RS-3, RS-1 | P2 | Legal/comms-approved templates available in IR runbook. |

## Phase 31-90 days (Build repeatability)

| Initiative | CSF Mapping | Priority | Measurable Outcome |
|---|---|---|---|
| 5. Expand telemetry onboarding for portal and legacy servers | DE-1, DE-3 | P1 | >90% critical assets sending required logs to SIEM. |
| 6. Launch patch SLA governance dashboard | PR-4, ID-4 | P1 | Monthly report shows critical patch SLA compliance >90%. |
| 7. Formalize privileged access recertification cadence | PR-1, GV-3 | P2 | Quarterly access review completed for privileged roles. |
| 8. Create incident playbooks for ransomware and portal compromise | RS-2, RS-4 | P1 | Two new tested playbooks added to IR library. |

## Phase 3-6 months (Integrate and test)

| Initiative | CSF Mapping | Priority | Measurable Outcome |
|---|---|---|---|
| 9. Integrate threat model into quarterly risk governance | ID-5, GV-4 | P2 | Quarterly risk forum includes threat scenario refresh. |
| 10. Introduce secure release checklist for portal changes | PR-7, ID-3 | P1 | 100% portal releases include security sign-off artifacts. |
| 11. Run cyber-focused BC/DR exercise | RC-2, RC-3, RC-1 | P2 | Exercise report validates restoration sequence and RTO targets. |

## Phase 6-12 months (Measure and optimize)

| Initiative | CSF Mapping | Priority | Measurable Outcome |
|---|---|---|---|
| 12. Implement post-incident and post-recovery action closure governance | RS-5, RC-4 | P3 | >90% actions closed by due date with evidence. |
| 13. Tune detections based on false-positive and dwell-time metrics | DE-2, DE-5 | P2 | Alert precision improves; triage time reduced by 25%. |
| 14. Expand third-party monitoring to critical existing suppliers | GV-5, ID-5 | P2 | Risk re-assessments completed for top 15 suppliers. |

## KPI dashboard suggestions
- MFA coverage rate (all users, privileged users).
- Critical patch SLA adherence.
- Detection use case coverage versus top threat scenarios.
- Mean time to triage (MTTT) and mean time to contain (MTTC).
- Backup restore success rate and tested critical service recovery times.
- Open versus closed remediation items by priority.
