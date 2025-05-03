import subprocess
from tqdm import tqdm
import time

def scan_vulns(ip):
    print(f"[*] Running vulnerability scan on {ip}...")
    for _ in tqdm(range(50), desc="Preparing vuln scan"):
        time.sleep(0.05)

    print(f"\n[~] Scanning {ip} for known vulnerabilities...\n")
    print("[INFO] This may take 1–4 minutes depending on the target.\n")

    try:
        process = subprocess.Popen(
            ['nmap', '-sV', '--script', 'vuln', ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        output = ""
        for line in process.stdout:
            print(line, end="")
            output += line

        process.wait()
        print("\n[✔] Vulnerability scan completed.")
        return output

    except KeyboardInterrupt:
        print("\n[✘] Scan aborted by user.")
        return "[!] Scan interrupted."

    except Exception as e:
        print(f"[!] Error: {e}")
        return "[!] Error during scan."
