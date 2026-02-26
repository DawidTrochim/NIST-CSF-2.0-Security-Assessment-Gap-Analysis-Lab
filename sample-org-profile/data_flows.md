# Key Data Flows and Trust Boundaries

This section summarizes high-value operational and security-relevant flows for Northbridge Supplies Ltd.

## Trust boundaries used
- **Boundary A:** Public Internet ↔ Azure customer portal edge
- **Boundary B:** Azure portal tier ↔ backend data services
- **Boundary C:** Corporate network ↔ remote workforce (VPN)
- **Boundary D:** End-user systems ↔ Microsoft 365 cloud
- **Boundary E:** Production systems ↔ backup and recovery environment
- **Boundary F:** Security telemetry sources ↔ centralized logging/SIEM

## Flow 1: Customer portal web access
- **Source:** External customer browsers
- **Destination:** Azure WAF → Azure App Service (`AZ-PORTAL-WEB-01`)
- **Purpose:** Order tracking, service requests, customer account access
- **Trust boundaries crossed:** Boundary A
- **Security considerations:** WAF policy quality, TLS, authentication controls, bot/abuse detection

## Flow 2: Portal application to backend data
- **Source:** Portal web/app/API tier
- **Destination:** Azure API + Azure SQL + Blob storage
- **Purpose:** Retrieve/update customer orders and case data
- **Trust boundaries crossed:** Boundary B
- **Security considerations:** Managed identity, least privilege DB roles, secrets handling, API abuse/rate limiting

## Flow 3: Microsoft 365 email and collaboration
- **Source:** User endpoints (laptops/desktops)
- **Destination:** M365 tenant services (Exchange, SharePoint, Teams)
- **Purpose:** Internal/external communication and file collaboration
- **Trust boundaries crossed:** Boundary D
- **Security considerations:** Phishing defense, conditional access, DLP, mailbox auditing

## Flow 4: Remote workforce access to internal resources
- **Source:** Remote user endpoints
- **Destination:** VPN gateway → on-prem resources (ERP, file server)
- **Purpose:** Operations, finance, and management workflows outside office
- **Trust boundaries crossed:** Boundary C
- **Security considerations:** MFA enforcement, split-tunnel policy, device compliance checks, session monitoring

## Flow 5: Warehouse operations to ERP/database
- **Source:** Warehouse desktops/shared devices
- **Destination:** On-prem ERP app and SQL database
- **Purpose:** Inventory updates, dispatch confirmation, label generation
- **Trust boundaries crossed:** Internal segmentation boundary (warehouse VLAN ↔ server VLAN)
- **Security considerations:** Shared account risk, endpoint hardening, lateral movement detection

## Flow 6: Backup and recovery pipeline
- **Source:** On-prem servers and key cloud workloads
- **Destination:** Backup server → offsite immutable vault
- **Purpose:** Business continuity and ransomware recovery
- **Trust boundaries crossed:** Boundary E
- **Security considerations:** Backup integrity, immutability, privileged access to backup console, restore test evidence

## Flow 7: Security logging and alerting pipeline
- **Source:** Firewall, EDR, Entra ID, Windows logs, portal logs
- **Destination:** SIEM workspace and ticketing workflow
- **Purpose:** Detection, triage, and investigation support
- **Trust boundaries crossed:** Boundary F
- **Security considerations:** Log completeness, normalization quality, retention, alert fatigue, handoff to responders
