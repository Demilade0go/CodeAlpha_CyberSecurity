from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("=================================")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")

        if TCP in packet and packet[TCP].payload:
            print(f"TCP Payload    : {bytes(packet[TCP].payload)}")
        elif UDP in packet and packet[UDP].payload:
            print(f"UDP Payload    : {bytes(packet[UDP].payload)}")

def start_sniffing():
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
