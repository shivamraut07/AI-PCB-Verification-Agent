# test_ollama.py
from langchain_ollama import OllamaLLM

# Connect to Ollama (make sure ollama serve is running in another terminal if needed)
llm = OllamaLLM(model="qwen2.5-coder:7b")

# Simple test prompt
prompt = "List 5 common PCB errors in ESP32 circuits, explain each briefly."
response = llm.invoke(prompt)
print(response)