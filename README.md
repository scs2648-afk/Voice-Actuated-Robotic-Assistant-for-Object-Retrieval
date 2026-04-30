# Voice-Controlled Assistive Robotic Arm

An Arduino-based robotic manipulator designed to help patients with upper-limb disabilities retrieve items using simple voice commands.

## Hardware
* **Microcontroller:** Arduino Mega 2560[cite: 1, 2]
* **Driver:** PCA9685 16-Channel PWM[cite: 1, 2]
* **Servos:** 3x MG996R (Arm) and 1x MG90S (Gripper)[cite: 1, 2]
* **Power:** External 5V 10A DC Supply[cite: 1, 2]

## Quick Start
1. **Hardware:** Connect the circuit as shown in `media/circuit_image.jpg`[cite: 1].
2. **Arduino:** Upload `robotic_arm_control.ino` to the Mega[cite: 2].
3. **Python:** 
   - Install libraries: `pip install speech_recognition sounddevice scipy pyttsx3 pyserial`[cite: 1, 2]
   - Run `python voice_control.py`[cite: 1, 2]
4. **Operation:** Click **START** and say "Medicine" (20°) or "Biscuit" (50°). The arm will deliver the item to the 150° position[cite: 2].

## Folder Structure
* `/Software`: Python voice interface script[cite: 1]
* `/Firmware`: Arduino code for servo control[cite: 2]
* `/Media`: Circuit diagrams and project demo video[cite: 1]
