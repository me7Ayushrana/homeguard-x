from flask import Flask, render_template, jsonify
from agents.network_sentinel import NetworkSentinelAgent
from agents.device_intelligence import DeviceIntelligenceAgent
from agents.risk_reasoning import RiskReasoningAgent
from agents.explanation_agent import ExplanationAgent
from agents.action_agent import ActionAgent

app = Flask(__name__)

# Initialize Agents
sentinel = NetworkSentinelAgent()
intelligence = DeviceIntelligenceAgent()
risk_engine = RiskReasoningAgent()
explainer = ExplanationAgent()
action_taker = ActionAgent()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/scan')
def scan_network():
    """
    Orchestrates the agent pipeline.
    """
    # 1. Sentinel loads data
    raw_devices = sentinel.scan_network()
    
    results = []
    
    for device in raw_devices:
        # 2. Intelligence enriches data
        enriched_device = intelligence.analyze_device(device)
        
        # 3. Risk Engine calculates score
        risk_data = risk_engine.assess_risk(enriched_device)
        
        # 4. Explainer creates narrative
        explanation = explainer.explain(enriched_device, risk_data)
        
        # 5. Action Agent suggests steps
        actions = action_taker.recommend_actions(risk_data)
        
        # Combine for Frontend
        results.append({
            "device": enriched_device,
            "risk": risk_data,
            "explanation": explanation,
            "actions": actions
        })
        
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
