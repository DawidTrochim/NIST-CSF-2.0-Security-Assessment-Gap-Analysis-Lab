# Northbridge Supplies Ltd
# NIST CSF 2.0 Audit & Gap Analysis Report

**Assessment period:** Synthetic scenario (4-week model)  
**Prepared by:** Cybersecurity Assessor (portfolio lab)  
**Classification:** Public-safe synthetic example

---

## 1) Executive summary
Northbridge Supplies Ltd has foundational cybersecurity capabilities aligned to a mid-sized operational business, but key control areas remain inconsistent. The current posture is strongest in **Protect** controls (MFA for privileged users, EDR coverage, backups), while **Detect**, **Respond**, and **Recover** capabilities require structured uplift.

The most significant risk drivers are:
1. Limited detection engineering and monitoring coverage for key attack paths.
2. Incomplete third-party security governance.
3. Partial incident playbooks and communications readiness.
4. Gaps in BC/DR cyber scenario integration and improvement tracking.

Overall, Northbridge’s security maturity is assessed at **1.7/4.0**, with a practical target of **2.8/4.0** in 6-12 months through phased remediation.

---

## 2) Scope and assumptions
### Scope
- Corporate IT estate (identity, endpoints, on-prem servers, networking).
- Azure-hosted customer portal services.
- Security tooling and incident response practices.
- Selected third-party dependency governance.

### Assumptions
- All evidence references are synthetic and sanitized.
- SOC coverage is limited outside business hours.
- OT/industrial systems are out of scope.
- Existing tool stack remains in place for near-term improvement plans.

---

## 3) Methodology
The assessment used a **CSF 2.0 function-aligned, evidence-driven scoring model**:
1. Define a pragmatic subset of CSF outcomes across Govern, Identify, Protect, Detect, Respond, Recover.
2. Map each outcome to observed implementation status and available evidence.
3. Score maturity (0-4) based on repeatability, documentation, and measurable operation.
4. Rate risk impact of gaps and assign priority (P1-P5).
5. Generate gap and remediation outputs for planning.

Evidence types considered included policy documentation, configuration snapshots, logs, tickets, training metrics, and backup reports.

---

## 4) Key findings (top 8)
1. **Detection engineering is underdeveloped** (DE-2), reducing early attack visibility.
2. **Third-party risk process is not formalized** (GV-5), creating external exposure.
3. **Portal monitoring normalization is incomplete** (DE-3), limiting cloud attack detection.
4. **Critical patching remains inconsistent** on legacy VM workloads (PR-4).
5. **Incident communications workflow is immature** (RS-3), risking delayed stakeholder response.
6. **Threat-informed risk review cadence is absent** (ID-5), reducing strategic prioritization quality.
7. **BC/DR exercises do not consistently include cyber scenarios** (RC-2).
8. **Lessons learned and closure tracking are informal** (RS-5, RC-4), weakening long-term resilience.

---

## 5) Heatmap summary (textual)
- **High-risk concentration:** Detect and Protect functions show the largest number of P1/P2 gaps.
- **Moderate-risk concentration:** Govern and Respond have mostly P2/P3 gaps with process ownership issues.
- **Lower-risk / stronger zones:** Security awareness (PR-6) and baseline governance artifacts (GV-1/GV-2) provide partial maturity anchors.

If visualized as a heatmap, the highest intensity cells would cluster around:
- DE-2, DE-3, PR-4, PR-7, GV-5, RS-2, RC-2.

---

## 6) Detailed findings table (top 12)

| Outcome | Status | Risk | Observation | Recommendation |
|---|---|---|---|---|
| GV-5 | Not Implemented | High | No formal supplier assurance workflow or risk tiering. | Implement third-party risk lifecycle with intake questionnaire and contract controls. |
| ID-1 | Partial | High | Asset inventory exists but cloud/SaaS reconciliation is incomplete. | Automate monthly reconciliation and assign owner attestation. |
| ID-4 | Partial | High | Vulnerability process exists but SLA adherence is inconsistent. | Define breach escalation and report SLA compliance monthly. |
| PR-2 | Partial | High | MFA not fully enforced for all user groups. | Enforce conditional access for all users with exception process. |
| PR-4 | Partial | High | Legacy workloads miss critical patch timelines. | Apply risk-based patch windows and temporary compensating controls. |
| PR-7 | Partial | High | Secure SDLC and cloud change assurance are inconsistent. | Introduce release security checklist and threat modeling trigger. |
| DE-1 | Partial | High | Centralized logging misses portions of server and app telemetry. | Expand ingestion for portal/app/server logs with retention policy enforcement. |
| DE-2 | Not Implemented | High | Detections rely on default vendor rules, limited tuning. | Build prioritized detection catalog for ransomware, phishing, and ATO paths. |
| DE-3 | Partial | High | Monitoring coverage map incomplete for portal and privileged activities. | Create monitoring control matrix and close top telemetry gaps. |
| RS-2 | Partial | High | Playbooks are limited mainly to phishing incidents. | Add ransomware, portal compromise, and insider misuse playbooks. |
| RS-3 | Not Implemented | High | External communication plan is not approved or tested. | Prepare legal/customer/regulatory templates and run tabletop drill. |
| RC-2 | Not Implemented | High | BC/DR exercises exclude realistic cyber failure modes. | Add cyber disruption scenarios and test restoration sequencing quarterly. |

---

## 7) Roadmap overview

### Phase 1 (0-30 days)
- Enforce remaining MFA coverage and conditional access baseline.
- Stand up top 10 detection use cases in SIEM.
- Publish supplier risk intake template and minimum contract clauses.
- Finalize incident communications templates.

### Phase 2 (31-90 days)
- Complete critical telemetry onboarding (portal, privileged actions, server logs).
- Expand incident playbooks and run tabletop for ransomware + portal compromise.
- Launch patch SLA governance dashboard with exception tracking.

### Phase 3 (3-6 months)
- Integrate threat model updates into quarterly risk reviews.
- Implement cloud/application release security checkpoints.
- Establish BC/DR cyber exercise cadence and after-action tracking.

### Phase 4 (6-12 months)
- Mature KPI/KRI reporting for board-level governance.
- Optimize detection tuning based on false positive trends.
- Demonstrate repeatable recovery performance against defined objectives.

---

## 8) Appendix: evidence approach
Assessment scoring was based on an evidence index mapped to each outcome. Evidence quality was rated by:
1. **Existence** (is evidence available?),
2. **Recency** (is it current?),
3. **Coverage** (does it represent all in-scope systems?),
4. **Operational proof** (does it show control actually operating?).

Where evidence was missing or weak, maturity scores were lowered to avoid overstating capability.
