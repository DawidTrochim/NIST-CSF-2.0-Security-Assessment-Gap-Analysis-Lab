# Sample Evidence Artifacts (Sanitized)

> Synthetic samples for demonstration only.

## 1) MFA enabled for admin roles
**Artifact type:** Identity platform configuration snapshot  
**Date:** 2026-01-12

```text
Policy: CA-ADMIN-MFA-REQUIRED
Scope: Role assignments [Global Admin, Privileged Role Admin, Security Admin]
Grant controls: Require multifactor authentication
State: Enabled
Excluded accounts: 0
```

## 2) Backup job report (critical systems)
**Artifact type:** Backup platform daily report  
**Date:** 2026-01-14

```text
Job group: Tier-1 Production
Assets: HQ-SQL-01, HQ-ERP-APP-01, AZ-SQL-PORTAL-01
Result: 3/3 successful
Offsite immutable copy: Completed
Last restore test: HQ-SQL-01 (2025-12-10) - PASS (RTO 2h 20m)
```

## 3) EDR alert sample
**Artifact type:** EDR detection event  
**Date:** 2026-01-08

```text
Alert ID: EDR-88421
Host: LAPTOP-NB-044
Severity: High
Detection: Suspicious encoded PowerShell execution
Action: Process terminated, host isolated automatically
Ticket: INC-1247 created (triage pending)
```

## 4) Phishing simulation summary
**Artifact type:** Awareness platform campaign report  
**Date:** 2025-Q4

```text
Campaign: Q4 Finance-themed phishing simulation
Recipients: 168
Click rate: 7.1%
Credential submission rate: 1.2%
Repeat clickers assigned targeted training: 9 users
```

## 5) Vulnerability remediation ticket sample
**Artifact type:** ITSM ticket extract  
**Date:** 2026-01-10

```text
Ticket: CHG-5632
Vulnerability: CVE-2025-XXXX (critical remote code execution)
Affected asset: HQ-ERP-APP-01
SLA target: 14 days
Actual closure: 19 days (SLA breach)
Mitigation during delay: WAF rule + restricted admin access
```

## 6) SIEM ingestion coverage note
**Artifact type:** SOC engineering checklist  
**Date:** 2026-01-11

```text
Ingested sources: Entra ID sign-ins, M365 audit, firewall logs, EDR alerts
Missing sources: Azure portal app diagnostics (partial), legacy Windows server logs
Retention baseline: 180 days
Owner action: Complete missing connectors by end of Q1
```
