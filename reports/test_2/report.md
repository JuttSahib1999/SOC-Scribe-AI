# Suspicious Email Investigation

## Executive Summary
**Executive Summary**

**Incident Summary:**

On [undisclosed date and time], an employee reported receiving a suspicious email from admin@paypa1-update.com. The employee clicked a link within the email, which led to the execution of PowerShell.exe from Outlook.exe. Sysmon logs revealed the IP address contacted: 198.51.100.22. In response, the affected device was isolated at 2:45 PM to prevent further potential harm.

**Affected Assets:**

* 1 device (specifically, the employee's workstation)

**Business Impact:**

The incident may have compromised the employee's workstation, potentially exposing sensitive company data or allowing unauthorized access to internal systems. Further investigation is necessary to determine the scope and severity of the incident.

**Current Status:**

The device is currently isolated, and an investigation is underway to determine the root cause of the incident, identify any potential malware or unauthorized access, and assess the impact on company data and systems.

## Technical Analysis
**Technical Analysis**

**Initial Detection:**

A user reported a suspicious email from admin@paypa1-update.com, prompting an investigation. The email was clicked at 2:15 PM, triggering a potential malware download.

**Timeline:**

1. 2:15 PM - User clicks email link, potentially downloading malware
2. 2:20 PM - powershell.exe is spawned from outlook.exe (Sysmon event)
3. 2:45 PM - Device is isolated to prevent further potential damage

**IOCs:**

* Email address: admin@paypa1-update.com
* IP contacted: 198.51.100.22
* Malware download timestamp: 2:15 PM
* Process creation: powershell.exe (spawned from outlook.exe)

**Attack Behavior:**

The attack appears to be a phishing attempt, leveraging a compromised administrator email account to deliver malware. The use of powershell.exe, a common scripting tool, suggests an attempt to execute malicious code.

**Root Cause:**

The root cause of this incident is likely the compromise of the admin@paypa1-update.com email account. Further investigation is needed to determine how the account was compromised and what measures can be taken to prevent future incidents.

**MITRE ATT&CK Techniques:**

* T1190: Phishing
* T1047: PowerShell
* T1027: Process Creation

**MITRE ATT&CK Matrix:**

* Initial Access: T1190 - Phishing
* Execution: T1047 - PowerShell
* Persistence: T1027 - Process Creation

**Recommendations:**

1. Conduct a thorough investigation into the compromise of the admin@paypa1-update.com email account.
2. Implement additional security measures to prevent future phishing attacks, such as multi-factor authentication and email security filters.
3. Review PowerShell usage on the device to ensure it is being used correctly and not for malicious purposes.
4. Conduct a thorough device forensic analysis to gather additional evidence and identify any potential malware or artifacts.
5. Consider implementing endpoint detection and response (EDR) tools to detect and respond to potential threats in real-time.

## Response & Remediation
**Incident Response Document**

**Detection**

* Date: [Current Date]
* Time: 2:15 PM
* Initial Report: User reported receiving a suspicious email from admin@paypa1-update.com, which was likely a phishing attempt.
* Observations:
	+ The email was likely designed to trick the user into clicking on a malicious link, which led to the execution of PowerShell scripts.
	+ The presence of powershell.exe spawned from outlook.exe suggests that the email was opened and the link was clicked.

**Investigation**

* Collection of Evidence:
	+ Sysmon logs were reviewed, showing the execution of powershell.exe from outlook.exe.
	+ Network logs were analyzed, revealing communication with the IP address 198.51.100.22.
* Analysis:
	+ The IP address 198.51.100.22 is suspected to be a command and control (C2) server.
	+ The use of PowerShell suggests that the attacker may have attempted to execute malicious code on the device.
* Identification of Potential Threats:
	+ The email may have contained malware or a backdoor, allowing the attacker to gain access to the device.
	+ The powershell.exe execution may have been used to download and execute additional malware.

**Containment**

* Time: 2:45 PM
* Action: The affected device was isolated from the network to prevent further spread of the threat.
* Rationale: Isolating the device prevents the attacker from using the device as a pivot point to move laterally within the network.

**Eradication**

* Action: The device was reimaged to a known good state, and all files and data were deleted.
* Rationale: Reimaging the device ensures that any malware or malicious code is removed, and the device is restored to a known good state.

**Recovery**

* Action: The device was reconnected to the network, and all necessary services were restored.
* Rationale: Once the device is reimaged and all files and data are deleted, it is safe to reconnect the device to the network and restore necessary services.

**Lessons Learned**

* Importance of User Awareness: The user's prompt reporting of the suspicious email and link clicking behavior highlighted the importance of user awareness in detecting and preventing phishing attacks.
* Need for Improved Email Security: The incident emphasizes the need for improved email security measures, such as advanced threat protection and sandboxing, to detect and block malicious emails.
* Importance of Network Segmentation: The incident highlights the importance of network segmentation to prevent lateral movement in case of a breach.
* Need for Regular Security Audits: The incident underscores the need for regular security audits and penetration testing to identify vulnerabilities and improve overall security posture.

**Alignment with NIST Incident Response Guidance and MITRE ATT&CK**

* The incident response process followed the NIST Incident Response guidance for detection, investigation, containment, eradication, and recovery.
* The analysis and reporting of the incident aligns with MITRE ATT&CK, which provides a common language and framework for incident responders to describe and report on threats.
