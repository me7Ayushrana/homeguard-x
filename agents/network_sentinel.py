import json
import os

class NetworkSentinelAgent:
    """
    Simulates a network scan by loading device data from a JSON file.
    In a real application, this would use nmap or scapy.
    """
    def __init__(self, data_path='data/sample_devices.json'):
        self.data_path = data_path

    def scan_network(self):
        """
        'Scans' the network (reads the JSON file) and returns raw device list.
        """
        print(f"[*] Sentinel Scanning network from: {self.data_path}")
        
        # Resolve absolute path relative to the app execution context if needed
        # For simplicity, assuming running from root
        if not os.path.exists(self.data_path):
             # Fallback for different running contexts
             self.data_path = os.path.join(os.getcwd(), 'homeguard_x_web', 'data', 'sample_devices.json')
             
        try:
            with open(self.data_path, 'r') as f:
                devices = json.load(f)
                return devices
        except FileNotFoundError:
            print(f"[!] Error: device data file not found at {self.data_path}")
            return []
