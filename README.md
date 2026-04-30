# Voice-Actuated-Robotic-Assistant-for-Object-Retrieval
A hands-free robotic solution for patients with upper-limb disabilities to retrieve medicine and snacks.

## Hardware Used
- Arduino Mega 2560
- PCA9685 Servo Controller
- 3x MG996R Servos (Base, Shoulder, Forearm)
- 1x MG90S Servo (Gripper)
- 5V 10A Power Supply

## How to Run
1. **Arduino:** Upload the code in `/Firmware` to your Mega.
2. **Python:** Install dependencies: `pip install speech_recognition sounddevice scipy pyttsx3 pyserial`.
3. **Execution:** Run the Python script and say "Medicine" or "Biscuit".
