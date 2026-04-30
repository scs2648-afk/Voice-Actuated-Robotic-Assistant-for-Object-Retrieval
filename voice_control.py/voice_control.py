import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
import threading
import tkinter as tk
import serial  # Required for Arduino communication

# --- ARDUINO CONNECTION ---
try:
    # Change 'COM3' to your actual port (e.g., 'COM5' or '/dev/ttyACM0')
    ser = serial.Serial('COM9', 9600, timeout=1) 
    time.sleep(2) # Wait for connection to stabilize
    print("✅ Connected to Arduino")
except:
    ser = None
    print("⚠️ Arduino NOT found. Check COM port.")

# --- VOICE ENGINE ---
try:
    import pyttsx3
    engine = pyttsx3.init()
    def speak(text):
        engine.say(text)
        engine.runAndWait()
except:
    def speak(text):
        print("🔊", text)

recognizer = sr.Recognizer()
fs = 44100
seconds = 3
running = False 

def voice_loop():
    global running
    print("🤖 System Ready")

    while running:
        try:
            print("\n🎤 Listening...")
            recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()

            recording_int16 = (recording * 32767).astype(np.int16)
            write("output.wav", fs, recording_int16)

            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio).lower()
                print("🧠 You said:", text)
            except:
                print("😅 Couldn't understand")
                continue

            # --- COMMAND LOGIC ---
            if any(word in text for word in ["medicine", "tablet", "pill"]):
                speak("Giving medicine")
                print("💊 Giving medicine")
                if ser: ser.write(b'M') # Send 'M' to Arduino

            elif any(word in text for word in ["biscuit", "snack", "food"]):
                speak("Giving biscuit")
                print("🍪 Giving biscuit")
                if ser: ser.write(b'B') # Send 'B' to Arduino

            elif "stop voice" in text:
                speak("Stopping system")
                running = False
                break
            
            time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)

def start_system():
    global running
    if not running:
        running = True
        threading.Thread(target=voice_loop, daemon=True).start()
        print("🟢 Voice Interface Started")

def stop_system():
    global running
    running = False
    print("🔴 Voice Interface Stopped")

# --- GUI ---
root = tk.Tk()
root.title("Voice Robot Controller")
root.geometry("300x250")

tk.Label(root, text="Robot Voice Control", font=("Arial", 12, "bold")).pack(pady=10)

start_btn = tk.Button(root, text="START LISTENING", command=start_system,
                      bg="green", fg="white", font=("Arial", 12), width=20)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="STOP LISTENING", command=stop_system,
                     bg="red", fg="white", font=("Arial", 12), width=20)
stop_btn.pack(pady=10)

root.mainloop()