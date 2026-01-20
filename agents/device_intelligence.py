class DeviceIntelligenceAgent:
    """
    Analyzes raw device data to identify device types and potential anomalies.
    """
    def analyze_device(self, device):
        """
        Enriches device data with intelligence.
        """
        # Basic Logic: Identify unknown vendors
        is_suspicious = False
        notes = []

        if "unknown" in device.get('vendor', '').lower():
            is_suspicious = True
            notes.append("Unknown Vendor: Device origin is obscure, increasing risk.")

        if device.get('encryption') == 'none':
             notes.append("Cleartext Traffic: Device creates unencrypted traffic.")

        # Intelligence Enrichment
        enriched_info = {
            "is_suspicious_vendor": is_suspicious,
            "intelligence_notes": notes
        }
        
        # Merge with original device data
        device.update(enriched_info)
        return device
