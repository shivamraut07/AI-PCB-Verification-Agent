# AI PCB Verification Agent

**Author:** Shivam Raut  
**Date:** February 5, 2026  
**Status:** v0.1 - Working Prototype ✅

## What It Does
Automatically analyzes PCB circuit descriptions and flags common design errors using local AI (Ollama + Qwen2.5-Coder-7B). No API costs, runs entirely on my laptop.

## Errors It Catches
- Missing decoupling capacitors near ICs
- LEDs without current-limiting resistors  
- Buttons/switches without pull-up/pull-down resistors
- Voltage level mismatches (5V ↔ 3.3V)
- Missing ground connections
- Power supply filtering issues

## Tech Stack
- **Python 3.11** - Core logic
- **LangChain** - Agent framework
- **Ollama** - Local LLM runtime (free, private)
- **Qwen2.5-Coder-7B** - AI model (4.7GB)

## Hardware
Built on: Lenovo LOQ (Ryzen 5 7235HS, 24GB RAM, RTX 3050)

## How to Run

### Prerequisites
1. Install [Ollama](https://ollama.com/download)
2. Pull model: `ollama pull qwen2.5-coder:7b`
3. Python 3.10+ with pip

### Setup
```bash
# Clone repo (when I push to GitHub)
git clone [your-repo-url]
cd PCB_Verifier_Agent

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run
```bash
python src/simple_agent.py
```

## Example Output
```
TEST CASE 1: Bad Circuit
------------------------------------------------------------
ESP32-WROOM-32 connected to:
- GPIO2 → LED → GND (no resistor)

🤖 AI Analysis:
**SEVERITY**: WARNING
**ERROR**: LED without current-limiting resistor
**FIX**: Add 330Ω resistor in series with GPIO2
```

## Learning Goals (Why I Built This)
1. **Verification Engineering Skills** - Automate manual PCB review tasks
2. **AI Integration** - Apply LLMs to hardware domain
3. **Portfolio Project** - Demonstrate problem-solving for placements 

## Roadmap (Next 4 Weeks)

**Week 1:** ✅ Basic text-input agent working  
**Week 2:** Add interactive mode + 10 more rules  
**Week 3:** Parse KiCad netlist files (.net format)  
**Week 4:** Integrate with ESP32 hardware testing  
**Future:** Offer as Fiverr service (₹500-2000/review)

## Why This Project Matters
- **Unique differentiator:** Most students show LED blink; I show AI-powered quality assurance
- **Industry relevance:** Verification engineers 
- **Scalable:** Can evolve into startup idea (AI PCB review SaaS)

---

**Status Log:**
- **Feb 5, 2026:** First working version (2 test cases passing)
- [Future updates will go here]

**Built with:** Coffee ☕ + late nights 🌙 + determination 💪