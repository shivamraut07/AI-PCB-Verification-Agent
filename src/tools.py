import re

def calculate_power_budget(circuit_description):
    """
    Parse circuit and estimate total current draw.
    Warn if power supply is insufficient.
    """
    
    # Known component current draws (typical values in mA)
    # ORDER MATTERS: More specific components first
    component_currents = [
        ("esp32-cam", 500),
        ("esp32-wroom", 200),
        ("esp32", 200),
        ("pir sensor", 50),
        ("hc-sr501", 50),
        ("pir", 50),
        ("isd1820", 100),
        # ("voice module", 100),  # Duplicate of ISD1820, disabled
        ("speaker", 200),
        ("servo", 500),
        ("sg90", 200),
        ("relay", 70),
        ("led", 20),
        ("oled", 20),
        ("lcd 16x2", 100),
        ("lcd", 100),
    ]
    
    description_lower = circuit_description.lower()
    
    total_current = 0
    components_found = []
    used_positions = []
    
    for component, current in component_currents:
        count = 0
        start = 0
        
        while True:
            pos = description_lower.find(component, start)
            if pos == -1:
                break
            
            overlap = False
            for used_start, used_end in used_positions:
                if not (pos >= used_end or pos + len(component) <= used_start):
                    overlap = True
                    break
            
            if not overlap:
                count += 1
                used_positions.append((pos, pos + len(component)))
            
            start = pos + 1
        
        if count > 0:
            total_current += current * count
            components_found.append({
                "name": component,
                "current_each": current,
                "count": count,
                "total": current * count
            })
    
    # Check against common power supplies
    power_supplies = {
        "ftdi": 500,
        "usb": 500,
        "ams1117": 800,
        "lm7805": 1500,
        "battery 9v": 500,
        "powerbank": 2000,
    }
    
    supply_type = "unknown"
    supply_capacity = 1000
    
    for supply, capacity in power_supplies.items():
        if supply in description_lower:
            supply_type = supply
            supply_capacity = capacity
            break
    
    result = {
        "total_current_ma": total_current,
        "components": components_found,
        "supply_type": supply_type,
        "supply_capacity_ma": supply_capacity,
        "status": "OK"
    }
    
    if total_current > supply_capacity * 0.9:
        result["status"] = "CRITICAL"
        result["warning"] = f"Total draw ({total_current}mA) exceeds {supply_type} capacity ({supply_capacity}mA)"
        result["fix"] = f"Use {int(total_current * 1.5)}mA+ rated supply (recommend 2A adapter)"
    elif total_current > supply_capacity * 0.7:
        result["status"] = "WARNING"
        result["warning"] = f"Total draw ({total_current}mA) near {supply_type} limit"
        result["fix"] = "Consider higher capacity supply or reduce simultaneous operations"
    
    return result


if __name__ == "__main__":
    print("="*70)
    print("POWER BUDGET CALCULATOR - TEST")
    print("="*70 + "\n")
    
    # Test Case 1: ESP32-CAM system with 2 speakers (mention speaker twice)
    test_circuit_1 = """
    ESP32-CAM with PIR sensor and ISD1820 voice module.
    Powered by FTDI programmer.
    First speaker connected to voice module output 1.
    Second speaker connected to voice module output 2.
    """
    
    print("TEST 1: ESP32-CAM Vehicle Detection System")
    print("-"*70)
    result = calculate_power_budget(test_circuit_1)
    
    print(f"📊 Total current draw: {result['total_current_ma']}mA")
    print(f"🔌 Power supply: {result['supply_type']} ({result['supply_capacity_ma']}mA capacity)")
    print(f"📈 Status: {result['status']}")
    
    if result.get('warning'):
        print(f"\n⚠️  WARNING: {result['warning']}")
        print(f"💡 Fix: {result['fix']}")
    
    print("\n📦 Component breakdown:")
    for comp in result['components']:
        print(f"   - {comp['name']}: {comp['current_each']}mA × {comp['count']} = {comp['total']}mA")
    
    print("\n" + "="*70 + "\n")
    
    # Test Case 2: Simple LED circuit
    test_circuit_2 = """
    Arduino Uno powered by USB.
    LED on pin 13, LED on pin 12, LED on pin 11 with resistors.
    """
    
    print("TEST 2: Simple Arduino LED Circuit")
    print("-"*70)
    result2 = calculate_power_budget(test_circuit_2)
    
    print(f"📊 Total current draw: {result2['total_current_ma']}mA")
    print(f"🔌 Power supply: {result2['supply_type']} ({result2['supply_capacity_ma']}mA capacity)")
    print(f"📈 Status: {result2['status']}")
    
    if result2.get('warning'):
        print(f"\n⚠️  WARNING: {result2['warning']}")
        print(f"💡 Fix: {result2['fix']}")
    else:
        print("\n✅ Power budget looks good!")
    
    print("\n📦 Component breakdown:")
    for comp in result2['components']:
        print(f"   - {comp['name']}: {comp['current_each']}mA × {comp['count']} = {comp['total']}mA")
    
    print("\n" + "="*70)