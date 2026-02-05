from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

print("Starting PCB Verification Agent...")
print("Connecting to Ollama...\n")

# Connect to your local Ollama
llm = ChatOllama(
    model="qwen2.5-coder:7b",
    temperature=0.3  # Lower = more focused, less creative
)

# The "brain" of your agent - tells it how to think
system_prompt = """You are a PCB verification expert with 10 years experience.

Your job: Analyze circuit descriptions for design errors.

Common errors to check:
1. Missing decoupling caps (0.1µF) near ESP32/microcontroller VDD pins
2. LEDs without current-limiting resistors
3. Voltage level mismatches (5V ↔ 3.3V without level shifter)
4. Button inputs without pull-up or pull-down resistors
5. Missing ground connections

Output format (use this EXACTLY):
**SEVERITY**: [CRITICAL / WARNING / INFO]
**ERROR**: [What's wrong]
**FIX**: [How to fix it]

If circuit looks good, say: "No critical errors found."
"""

def check_circuit(description):
    """Send circuit to AI for analysis"""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Analyze this circuit:\n\n{description}")
    ]
    
    response = llm.invoke(messages)
    return response.content

# ===== TEST CASES =====
if __name__ == "__main__":
    print("="*60)
    print("PCB VERIFICATION AGENT - v0.1")
    print("="*60 + "\n")
    
    # Test Case 1: BAD circuit (multiple errors)
    bad_circuit = """
ESP32-WROOM-32 connected to:
- 3.3V power from AMS1117 regulator
- GPIO2 → LED (red) → GND (no resistor)
- GPIO4 → tactile button → GND (no pull-up)
- No capacitors anywhere in the circuit
"""
    
    print("TEST CASE 1: Bad Circuit")
    print("-" * 60)
    print(bad_circuit)
    print("-" * 60)
    print("\n🤖 AI Analysis:\n")
    result1 = check_circuit(bad_circuit)
    print(result1)
    print("\n" + "="*60 + "\n")
    
    # Test Case 2: GOOD circuit
    good_circuit = """
ESP32-WROOM-32 circuit:
- 3.3V power from AMS1117-3.3 regulator
- 0.1µF ceramic capacitor between ESP32 VDD (pin 2) and GND
- GPIO2 → 330Ω resistor → LED (red, 2V drop) → GND
- GPIO4 → tactile button → GND, with 10kΩ pull-up to 3.3V
- Proper ground plane on PCB
"""
    
    print("TEST CASE 2: Good Circuit")
    print("-" * 60)
    print(good_circuit)
    print("-" * 60)
    print("\n🤖 AI Analysis:\n")
    result2 = check_circuit(good_circuit)
    print(result2)
    print("\n" + "="*60)