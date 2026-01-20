class ExplanationAgent:
    """
    Translates technical risk factors into human-readable narratives.
    """
    def explain(self, device, risk_assessment):
        """
        Generates a summary string.
        """
        level = risk_assessment['level']
        reasons = risk_assessment['analysis_reasons']
        device_name = f"{device['vendor']} {device['device_type']}"
        
        explanation = f"We analyzed your {device_name}. "
        
        if level == "Safe":
            explanation += "It appears to be secure. Uses valid encryption and no dangerous ports were found."
            return explanation

        if level == "High":
             explanation += "WARNING: critical security gaps found. "
        elif level == "Medium":
             explanation += "Caution advised. Some settings may be risky. "
        else:
             explanation += "Minor issues detected. "

        # Summarize reasons
        reason_texts = []
        for r in reasons:
            trigger = r['trigger']
            title = r['detail']['title']
            reason_texts.append(f"{title} ({trigger})")
        
        if reason_texts:
            explanation += "Key issues: " + ", ".join(reason_texts) + "."
        
        # Add family impact specifically
        if "Camera" in device['device_type'] and level in ["High", "Medium"]:
            explanation += " FAMILY RISK: Since this is a camera, these vulnerabilities could allow strangers to view your home feed."
        
        return explanation
