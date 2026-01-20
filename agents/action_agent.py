class ActionAgent:
    """
    Suggests concrete next steps for the user.
    """
    def recommend_actions(self, risk_assessment):
        """
        Returns a list of action strings.
        """
        actions = []
        
        reasons = risk_assessment.get('analysis_reasons', [])
        
        for r in reasons:
            mitigation = r['detail'].get('mitigation')
            if mitigation:
                actions.append(mitigation)
        
        if not actions and risk_assessment['level'] != "Safe":
             actions.append("Review the device manual for security settings.")
             
        if risk_assessment['level'] == "Safe":
            actions.append("No action needed. Keep firmware updated.")

        return list(set(actions)) # Remove duplicates
