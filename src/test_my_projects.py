from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.3)

system_prompt = """You are a PCB verification expert with 10 years experience.

Analyze circuit descriptions for design errors:
1. Missing decoupling caps near ICs
2. Missing current-limiting resistors for LEDs
3. Voltage level mismatches (5V ↔ 3.3V)
4. Button/sensor inputs without pull-ups
5. Missing ground connections
6. Power supply filtering
7. I2C lines without pull-ups
8. Shared power rail issues (multiple modules on one supply)

Output format:
**SEVERITY**: [CRITICAL / WARNING / INFO]
**ERROR**: [What's wrong]
**FIX**: [How to fix it]
**COMPONENT**: [Which part affected]

If good, say: "No critical errors found."
"""

vehicle_detection_circuit = """
ESP32-CAM Vehicle Detection System (5V):
* 5V (from FTDI / programmer board) → ESP32-CAM 5V pin
* GND (common ground) → ESP32-CAM GND, PIR sensor GND, Voice module GND

PIR Motion Sensor:
* VCC → 5V
* GND → GND
* OUT → ESP32-CAM GPIO (motion trigger pin)

ESP32-CAM Module:
* Onboard Camera → Captures image on PIR trigger
* Wi-Fi (built-in) → Sends Base64 encoded image to Hugging Face API
* UART pins (U0R / U0T) → FTDI programmer (during programming only)
* GPIO output pin → Voice module trigger input

Voice Alert Module (ISD1820):
* VCC → 5V
* GND → GND
* PLAY / Trigger pin → ESP32-CAM GPIO output
* SP+ / SP- → Two mini speakers (parallel connection)

Maintenance Mode (Software-Based):
* ESP32-CAM IP address → Accessed via web browser
* Same Wi-Fi network → Required for live camera streaming
* Live stream → Used to align camera angle for no-parking area

System Logic Summary:
* PIR detects motion → ESP32-CAM captures image
* Image encoded in Base64 → Sent to object detection API
* Vehicle detected → Voice alert triggered
* No vehicle → System waits for next motion event
"""

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=f"Analyze this multi-module system:\n\n{vehicle_detection_circuit}")
]

print("🤖 Analyzing ESP32-CAM Vehicle Detection System...\n")
print("="*70)

response = llm.invoke(messages)
print(response.content)

print("="*70)


