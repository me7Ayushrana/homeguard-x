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
        'Scans' the network.
        Update: Now adds RANDOMIZATION to mimic a live environment for the demo.
        """
        print(f"[*] Sentinel Scanning network from: {self.data_path}")
        
        if not os.path.exists(self.data_path):
             self.data_path = os.path.join(os.getcwd(), 'homeguard_x_web', 'data', 'sample_devices.json')
             
        try:
            with open(self.data_path, 'r') as f:
                all_devices = json.load(f)
                
            # --- DEMO DYNAMICS ---
            # Randomly pick 3 to 5 devices to show (makes it feel like it's actually scanning)
            import random
            num_devices = random.randint(3, len(all_devices))
            selected_devices = random.sample(all_devices, num_devices)
            
            # Add some "live" variation to IPs
            for dev in selected_devices:
                # Keep prefix 192.168.1. but randomize last digit slightly
                parts = dev['ip_address'].split('.')
                parts[3] = str(random.randint(2, 254))
                dev['ip_address'] = ".".join(parts)
                
            return selected_devices

        except FileNotFoundError:
            print(f"[!] Error: device data file not found at {self.data_path}")
            return []
