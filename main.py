from scanner.discovery import discover_devices
from scanner.portscan import scan_ports
from scanner.vulnscan import scan_vulns
from utils.ui import print_menu, show_welcome, confirm_permission

def get_valid_device_index(devices):
    while True:
        try:
            index = int(input("Enter device number: ")) - 1
            if 0 <= index < len(devices):
                return index
            else:
                print("❌ Invalid number. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    show_welcome()

    if not confirm_permission():
        print("Exiting... You must have permission to scan a network.")
        return

    while True:
        choice = print_menu("Main Menu", ["Scan Network", "Exit"])
        if choice == 1 or choice == -1:
            break

        devices = discover_devices()
        if not devices:
            print("No devices found.")
            continue

        print("\nDiscovered Devices:")
        for idx, dev in enumerate(devices):
            print(f"[{idx+1}] {dev['ip']} | {dev['mac']} | {dev['name']} | {dev['geo']} | {dev['isp']}")

        scan_choice = print_menu("Port Scan", ["Scan all devices", "Scan specific device", "Exit"])
        if scan_choice == 2 or scan_choice == -1:
            break

        if scan_choice == 0:
            for dev in devices:
                ports, os_name, risk = scan_ports(dev['ip'])
                print(f"{dev['ip']} open ports: {ports} | OS: {os_name} | RISK: {risk}")

        elif scan_choice == 1:
            index = get_valid_device_index(devices)
            ip = devices[index]['ip']
            ports, os_name, risk = scan_ports(ip)
            print(f"{ip} open ports: {ports} | OS: {os_name} | RISK: {risk}")

            vuln_choice = print_menu("Vulnerability Scan", ["Scan this device", "Skip", "Exit"])
            if vuln_choice == 0:
                result = scan_vulns(ip)
                print(result)
            elif vuln_choice == 2:
                break

    print("Exiting...")
    print("Thank you <3")

if __name__ == "__main__":
    main()
