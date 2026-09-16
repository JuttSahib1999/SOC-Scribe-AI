import json

def get_synthetic_incident():
    return json.dumps({
        "event_id": "SEC-9921-X",
        "alert_name": "Multiple Failed Logins Followed by Success",
        "timestamp": "08:45:12 UTC",
        "source_ip": "192.168.1.55 (Internal) / 203.0.113.45 (External)",
        "target_account": "admin_service_acc",
        "analyst_notes": "Detected 500 failed login attempts via RDP over 3 hours. Followed by a successful login and an immediate PowerShell execution downloading a payload from an unknown domain.",
        "iocs": ["203.0.113.45", "http://malicious-domain[.]xyz/payload.exe"],
        "status": "Contained - Endpoint Isolated"
    }, indent=2)