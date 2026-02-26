# Organization Overview: Northbridge Supplies Ltd

## Company snapshot
- **Name:** Northbridge Supplies Ltd
- **Sector:** UK-based B2B logistics and warehousing
- **Size:** ~180 staff
- **Operating model:** 2 physical sites (HQ + warehouse/distribution site) and hybrid remote workforce

## Business model
Northbridge Supplies Ltd provides warehousing, stock management, and time-critical B2B distribution for enterprise customers in retail, light manufacturing, and healthcare support sectors. Revenue depends on reliable order processing, inventory accuracy, and delivery SLAs.

## Technology environment
- **Identity & productivity:** Microsoft 365 and Entra ID
- **Endpoints:** Windows laptops/desktops for office and operations users
- **On-prem infrastructure:** Small VM cluster supporting legacy line-of-business workloads
- **Cloud application:** Public customer portal hosted on Azure for order tracking and service requests
- **Network:** Basic perimeter firewall, site-to-site connectivity, remote access capability
- **Security operations:** Limited SOC capacity (primarily business-hours triage with outsourced support for major incidents)

## Business drivers
1. **Operational uptime** for warehouse and dispatch workflows.
2. **Customer portal availability** for order visibility and ticketing.
3. **Compliance confidence** driven by enterprise customer security questionnaires and contractual obligations.

## Security context
Northbridge has made practical foundational investments (MFA for privileged users, EDR on most endpoints, backups), but governance and detection engineering are less mature. The organization is now prioritizing measurable control uplift to reduce ransomware and credential abuse risk while maintaining service continuity.
