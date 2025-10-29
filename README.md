# 💡 Raspberry Pi Pico W – LED Brightness Control using PWM (MicroPython)

This project demonstrates how to control the **brightness of an LED** using **PWM (Pulse Width Modulation)** on the **Raspberry Pi Pico W**, programmed in **MicroPython** via **Thonny IDE**.

---

## ⚙️ What is PWM?
**PWM (Pulse Width Modulation)** rapidly switches a digital output between HIGH and LOW.  
By adjusting how long the signal stays HIGH (the **duty cycle**), you can simulate an analog voltage — controlling LED brightness, motor speed, or audio tone intensity.

- **0% Duty Cycle (0)** → LED OFF  
- **100% Duty Cycle (65535)** → LED FULL ON  

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Raspberry Pi Pico W | 1 | Microcontroller board |
| LED | 1 | Any color |
| 220Ω Resistor | 1 | Current limiting for LED |
| Jumper Wires | Few | Connections |
| Breadboard | 1 | Optional |

---

## 🧠 Circuit Connection

| LED Pin | Pico W Pin | Description |
|----------|-------------|-------------|
| Anode (+) | GPIO17 | PWM Output |
| Cathode (–) | GND | Ground |

💡 *Always use a resistor (around 220 Ω) in series with your LED.*

---
while True:
    pwm.duty_u16(65535)  # 100% duty cycle (LED fully ON)
