# Threat Model (Scenario-Based)

## Threat 1: Ransomware impacting operations
- **Attack path summary:** Phishing or remote access compromise leads to endpoint execution, credential theft, lateral movement to file/ERP servers, encryption and service outage.
- **Likely impact:** Warehouse disruption, delayed shipments, customer SLA breaches, recovery cost escalation.
- **Likely indicators:** Suspicious PowerShell activity, mass file rename/write, disabled security tooling, unusual SMB traffic.
- **Affected CSF Functions:** Identify, Protect, Detect, Respond, Recover.
- **Suggested detection ideas:**
  - Alert on rapid file extension changes and shadow copy deletion.
  - Correlate EDR high-severity detections with privileged login anomalies.
  - Monitor backup job deletion/modification events.

## Threat 2: Credential phishing and account takeover
- **Attack path summary:** User receives phishing email, enters credentials into fake portal, attacker bypasses weak MFA coverage and accesses M365 or VPN.
- **Likely impact:** Business email compromise, fraudulent requests, data exfiltration, internal spread through trusted channels.
- **Likely indicators:** Impossible travel, unusual MFA prompts, mailbox forwarding rule creation, unusual OAuth app consent.
- **Affected CSF Functions:** Govern, Protect, Detect, Respond.
- **Suggested detection ideas:**
  - Alert on risky sign-ins and unfamiliar geolocation.
  - Monitor mailbox rule and inbox permission changes.
  - Trigger high-priority tickets for impossible-travel + MFA fatigue patterns.

## Threat 3: Supplier compromise and third-party access abuse
- **Attack path summary:** Compromised vendor account or remote support channel is used to access systems without adequate monitoring.
- **Likely impact:** Unauthorized changes, malware delivery, data leakage via trusted integration paths.
- **Likely indicators:** Off-hours supplier account use, anomalous remote admin tool activity, unexpected config changes.
- **Affected CSF Functions:** Govern, Identify, Protect, Detect.
- **Suggested detection ideas:**
  - Track privileged sessions by supplier identities.
  - Require and alert on just-in-time approval for third-party maintenance windows.
  - Baseline remote support tool usage and alert on deviations.

## Threat 4: Public portal exploit
- **Attack path summary:** Vulnerability in portal web/API stack exploited for data access, service disruption, or web shell behavior.
- **Likely impact:** Customer data exposure, portal downtime, reputational damage, contractual penalties.
- **Likely indicators:** WAF spikes, unusual API request patterns, elevated 5xx errors, suspicious process execution in app environment.
- **Affected CSF Functions:** Identify, Protect, Detect, Respond, Recover.
- **Suggested detection ideas:**
  - Alert on high-rate failed requests and payload signatures.
  - Track admin/configuration changes in cloud resources.
  - Detect sudden data export volume anomalies from portal database.

## Threat 5: Insider misuse (malicious or negligent)
- **Attack path summary:** Authorized user abuses broad access or mishandles sensitive data through email/share links/removable media.
- **Likely impact:** Confidentiality breach, legal exposure, trust impact with enterprise customers.
- **Likely indicators:** Large downloads, unusual access to HR/contract files, repeated policy violations, off-hours access.
- **Affected CSF Functions:** Govern, Identify, Protect, Detect, Respond.
- **Suggested detection ideas:**
  - Alert on high-volume data movement from sensitive repositories.
  - Enforce and monitor DLP policy violations.
  - Review privileged and sensitive access monthly with manager attestation.

## Threat 6: Cloud misconfiguration exposure
- **Attack path summary:** Misconfigured storage/account/network policy exposes data or management plane to internet abuse.
- **Likely impact:** Data leakage, unauthorized access, potential foothold for broader compromise.
- **Likely indicators:** External discovery alerts, unusual authentication attempts, sudden resource policy drift.
- **Affected CSF Functions:** Govern, Identify, Protect, Detect.
- **Suggested detection ideas:**
  - Continuous cloud configuration checks against baseline.
  - Alert on public access settings enabled for sensitive storage.
  - Daily review of high-risk cloud control plane changes.
