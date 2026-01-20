import json
import os

class RiskReasoningAgent:
    """
    The 'Brain'. Logic engine that scores risk based on attributes and rules.
    """
    def __init__(self, rules_path='data/risk_rules.json'):
        self.rules_path = rules_path
        self.rules = self._load_rules()

    def _load_rules(self):
        # Resolve path similar to sentinel
        if not os.path.exists(self.rules_path):
             self.rules_path = os.path.join(os.getcwd(), 'homeguard_x_web', 'data', 'risk_rules.json')
        
        try:
            with open(self.rules_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Error loading rules: {e}")
            return {}

    def assess_risk(self, device):
        """
        Calculates a risk score (0-100) and level (Low, Medium, High).
        """
        score = 0
        reasons = []

        # 1. Check Open Ports
        open_ports = device.get('open_ports', [])
        port_rules = self.rules.get('ports', {})
        
        for port in open_ports:
            str_port = str(port)
            if str_port in port_rules:
                rule = port_rules[str_port]
                # Add score based on level (Arbitrary weights for MVP)
                if rule['risk_level'] == 'High': score += 30
                elif rule['risk_level'] == 'Medium': score += 15
                else: score += 5
                
                reasons.append({
                    "type": "port_risk",
                    "detail": rule,
                    "trigger": f"Port {port}"
                })

        # 2. Check Attributes (Default Password, Encryption)
        attr_rules = self.rules.get('attributes', {})
        
        # Default Password Check
        if device.get('default_password_detected'):
            rule = attr_rules.get('default_password_detected', {}).get('true')
            if rule:
                score += rule.get('risk_score_impact', 0)
                reasons.append({
                    "type": "auth_risk",
                    "detail": rule,
                    "trigger": "Default Password"
                })

        # Encryption Check
        enc = device.get('encryption', 'none')
        enc_rule = attr_rules.get('encryption', {}).get(enc)
        if enc_rule:
            score += enc_rule.get('risk_score_impact', 0)
            reasons.append({
                "type": "encryption_risk",
                "detail": enc_rule,
                "trigger": f"Encryption: {enc}"
            })
            
        # Firmware Check
        # MVP Logic: if not 'LATEST' or 'Auto-Update', consider it potential risk
        fw = device.get('firmware_version', '')
        if fw not in ['LATEST', 'Auto-Update'] and 'beta' in fw:
             # Hardcoded rule for beta/custom logic simulation
             rule = attr_rules.get('firmware_version', {}).get('obsolete') # Mapping beta to obsolete for demo
             if rule:
                 score += 10 # slightly less than obsolete
                 reasons.append({
                    "type": "software_risk",
                    "detail": rule,
                    "trigger": f"Firmware: {fw}"
                 })


        # Cap score at 100
        score = min(score, 100)
        
        # Determine Level
        if score >= 60: risk_level = "High"
        elif score >= 30: risk_level = "Medium"
        else: risk_level = "Low"

        # Safe Device handling (ensure low score for "safe" looking devices)
        if score == 0:
            risk_level = "Safe"

        return {
            "score": score,
            "level": risk_level,
            "analysis_reasons": reasons
        }
