import nmap
from tqdm import tqdm
import time

def assess_risk(ports):
    risky_ports = [21, 23, 25, 110, 445, 3389]
    score = sum(1 for p in ports if p in risky_ports)
    if score >= 3:
        return "HIGH"
    elif score == 2:
        return "MEDIUM"
    elif score == 1:
        return "LOW"
    else:
        return "SAFE"

def scan_ports(ip):
    print(f"[*] Scanning ports for {ip}...")
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-T4 -F -O')  # Fast scan + OS detection

    if ip not in nm.all_hosts():
        print(f"[!] No response from {ip}. Skipping...")
        return [], "Unknown", "Unknown"

    open_ports = []
    all_protocols = nm[ip].all_protocols()

    for proto in tqdm(all_protocols, desc=f"Scanning protocols on {ip}"):
        ports = list(nm[ip][proto].keys())
        for port in ports:
            time.sleep(0.01)
            state = nm[ip][proto][port]['state']
            if state == "open":
                open_ports.append(port)

    os_match = nm[ip].get("osmatch", [])
    os_name = os_match[0]['name'] if os_match else "Unknown"

    risk_level = assess_risk(open_ports)
    return open_ports, os_name, risk_level
