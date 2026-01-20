# HomeGuard X - Agentic AI Web Guardian

## Project Overview
HomeGuard X is a **web-based security advisor** designed for the **eRaksha Hackathon 2026**. It demonstrates how **Agentic AI** can be used to protect home networks and families from IoT risks.

The application simulates a home network environment and uses a pipeline of intelligent Python agents to analyze devices, reason about their risks, and explain complex security concepts in simple English.

## Features
- **Agentic Logic**: 5 specialized agents working in a pipeline (Sentinel -> Intelligence -> Risk -> Explanation -> Action).
- **Privacy First**: No real data is sent to the cloud.
- **Family Focused**: Highlights risks specifically related to child safety (e.g., insecure baby monitors).
- **Explainable AI**: No "black box" decisions. Every risk score is backed by clear, rule-based reasoning.

## How to Run Locally

1. **Prerequisites**
   - Python 3.8+
   - pip

2. **Installation**
   ```bash
   cd homeguard_x_web
   pip install -r requirements.txt
   ```

3. **Running the App**
   ```bash
   python app.py
   ```
   The app will start at `http://127.0.0.1:5000`.

4. **Usage**
   - Open your browser to the URL above.
   - Click **"Analyze Home Network"**.
   - Watch the agents process the simulated environment and present the findings.

## Transparency & MVP Scope
> [!IMPORTANT]
> **This is a Hackathon MVP prototype.**
> 
> - **Simulated Scanning**: Actual network scanning is restricted in browser environments. This app uses a **simulated dataset** (`data/sample_devices.json`) to demonstrate the *logic* and *reasoning capabilities* of the system.
> - **Rule-Based Agents**: The current agents use deterministic logic tables (`data/risk_rules.json`) rather than LLMs to ensure reliability and speed for the demo.

## Project Structure
- `agents/`: Python modules containing the logic for each agent.
- `data/`: JSON files defining the simulation acts and risk rules.
- `app.py`: Flask entry point.
- `static/style.css`: Custom glassmorphism design.
