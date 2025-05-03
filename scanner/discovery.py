from scapy.all import ARP, Ether, srp
import socket
import requests

def get_geo_info(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        city = res.get("city", "Unknown")
        country = res.get("country", "Unknown")
        isp = res.get("isp", "Unknown")
        return f"{city}, {country}", isp
    except:
        return "Unknown", "Unknown"

def discover_devices(ip_range="192.168.0.1/24"):
    print("[*] Scanning network for devices...")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except:
            hostname = "Unknown"
        geo, isp = get_geo_info(received.psrc)
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'name': hostname,
            'geo': geo,
            'isp': isp
        })
    return devices
