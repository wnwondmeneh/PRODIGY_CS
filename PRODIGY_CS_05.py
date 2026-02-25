

from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_handler(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        protocol_name = "OTHER"
        src_port = dst_port = "-"

        if TCP in packet:
            protocol_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        payload_preview = ""
        if Raw in packet:
            raw_bytes = bytes(packet[Raw].load)
            # Show only first 50 bytes to reduce sensitivity
            payload_preview = raw_bytes[:50].hex()

        print(f"[{timestamp}] {protocol_name} "
              f"{src_ip}:{src_port} -> {dst_ip}:{dst_port} "
              f"Payload(hex, first 50B): {payload_preview}")

def main():
    print("=== Educational Packet Sniffer ===")
    print("Use ONLY on networks you own or have permission to analyze.")
    print("Press Ctrl+C to stop.\n")

    # iface=None lets Scapy choose the default interface
    sniff(prn=packet_handler, store=False)

if __name__ == "__main__":
    main()