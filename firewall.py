from scapy.all import sniff, IP, TCP, UDP
import json
from logger import log_packet
# from iptables_helper import apply_block_rule  # Optional

with open("rules.json") as f:
    rules = json.load(f)

def check_rules(packet):
    if IP in packet:
        src_ip = packet[IP].src
        protocol = None
        sport = None

        if TCP in packet:
            protocol = "TCP"
            sport = packet[TCP].sport
        elif UDP in packet:
            protocol = "UDP"
            sport = packet[UDP].sport

        for rule in rules.get("block", []):
            if rule["ip"] == src_ip and rule["port"] == sport and rule["protocol"] == protocol:
                log_packet(packet, "Blocked packet")
                # apply_block_rule(src_ip, sport, protocol)
                return False

        for rule in rules.get("allow", []):
            if rule["ip"] == src_ip and rule["port"] == sport and rule["protocol"] == protocol:
                return True

        log_packet(packet, "Suspicious packet")
    return True

def packet_callback(packet):
    check_rules(packet)

if __name__ == "__main__":
    print("Starting Personal Firewall...")
    sniff(prn=packet_callback, store=0)
