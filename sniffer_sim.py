# File: network_sniffer/sniffer_sim.py
# Title: Simulated Network Packet Sniffer
# Author: ishma-cbysec

import random

# Simulated packets
packets = [
    {"src": "192.168.1.5", "dst": "192.168.1.1", "protocol": "TCP", "length": 74},
    {"src": "192.168.1.5", "dst": "224.0.0.251", "protocol": "UDP", "length": 90},
    {"src": "10.0.0.2", "dst": "10.0.0.1", "protocol": "ICMP", "length": 60},
    {"src": "172.16.0.10", "dst": "172.16.0.1", "protocol": "TCP", "length": 120},
]

def packet_callback(packet):
    print(f"Packet: {packet['protocol']} {packet['src']} > {packet['dst']}")
    print(f"Source IP: {packet['src']}")
    print(f"Destination IP: {packet['dst']}")
    print(f"Protocol: {packet['protocol']}")
    print(f"Length: {packet['length']}\n")

# Simulate capturing 5 random packets
for _ in range(5):
    packet = random.choice(packets)
    packet_callback(packet)
