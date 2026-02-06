# AI PCB Verification Agent

📊 **Progress Tracker:** [View on Notion](https://www.notion.so/AI-PCB-Verification-Agent-2fe7eafe1a35806fa778fd0b65e244cd?source=copy_link)

**Status:** v0.1 - Working Prototype ✅  
**Author:** Shivam Raut 
**Date:** February 6, 2026

## What It Does
Automatically analyzes PCB circuit descriptions and flags common design errors using local AI (Ollama + Qwen2.5-Coder-7B). 

Catches:
- Missing decoupling capacitors
- LEDs without current-limiting resistors
- Floating GPIO pins (missing pull-ups/pull-downs)
- Voltage level mismatches (5V ↔ 3.3V)
- Power supply issues

## Tech Stack
- Python 3.11
- LangChain + Ollama (local LLM, no API costs)
- Qwen2.5-Coder-7B model

## Example Output

Tested on ESP32-CAM Vehicle Detection System:
```
**SEVERITY**: CRITICAL
**ERROR**: Missing decoupling capacitors near ESP32-CAM
**FIX**: Add 0.1µF ceramic cap between VDD and GND
**COMPONENT**: ESP32-CAM

**SEVERITY**: WARNING
**ERROR**: Total current draw (1050mA) exceeds FTDI limit (500mA)
**FIX**: Use external 5V 2A power supply
```
## Demo Screenshots

### Agent in Action
![Agent analyzing circuit](screenshots/agent_output_demo.png)

### Project Structure
![Code organization](screenshots/code_structure.png)

## How to Run

### Prerequisites
1. Install [Ollama](https://ollama.com/download)
2. Pull model: `ollama pull qwen2.5-coder:7b`
3. Python 3.10+

### Setup
```bash
# Clone repo
git clone https://github.com/shivamraut07/AI-PCB-Verification-Agent.git
cd AI-PCB-Verification-Agent

# Create virtual environment
python -m venv venv

# Activate venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Agent
```bash
python src/simple_agent.py
```

## Project Structure
```
PCB_Verifier_Agent/
├── src/
│   ├── simple_agent.py       # Main agent code
│   ├── test_my_project.py    # Real project test (ESP32-CAM)
│   └── tools.py              # Power budget checker (coming soon)
├── screenshots/              # Demo images
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Roadmap

**Week 1:** ✅ Basic agent working (catches 6+ error types)  
**Week 2:** ⏳ Power budget analysis  
**Week 3:** ⏳ Parse KiCad netlist files  
**Week 4:** ⏳ Hardware integration (ESP32 testing)

## Why This Project Matters

- **Portfolio differentiator:** Most students show LED blink; I show AI-powered quality assurance
- **Industry relevance:** Verification engineers earn 15-25 LPA
- **Real impact:** Catches errors before PCB fabrication (saves ₹5000+ per board spin)

---

**Built with:** ☕ Late nights + 🧠 AI + ⚡ Embedded systems knowledge