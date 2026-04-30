# Voice-Actuated-Robotic-Assistant-for-Object-Retrieval
pip install -r requirements.txt
    ```
3.  UpdateHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connectionHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the applicationHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ positionHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUIHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**Here is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get theHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*Here is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning homeHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematicHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and imagesHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and images[cite: 1].
*   `robotic_arm_control.inoHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and images[cite: 1].
*   `robotic_arm_control.ino/`: Arduino firmware for servo kinematicsHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and images[cite: 1].
*   `robotic_arm_control.ino/`: Arduino firmware for servo kinematics[cite: 2].
*   `voice_control.py/`: Python GUI and speech recognition engineHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and images[cite: 1].
*   `robotic_arm_control.ino/`: Arduino firmware for servo kinematics[cite: 2].
*   `voice_control.py/`: Python GUI and speech recognition engine[cite: 1, 2].
*   `requirements.txt`: Python library dependenciesHere is a comprehensive and professional `README.md` file designed for your GitHub repository. It incorporates the project title, short description, hardware specifics, and usage instructions based on your uploaded files.

---

# Voice-Actuated Assistive Robotic Manipulator

**Assistive Object Retrieval and Proximity Delivery for Patients with Upper-Limb Disabilities**

This project provides a hands-free solution for individuals with severe motor impairments to interact with their environment[cite: 1, 2]. By using voice commands through a laptop interface, users can instruct a robotic arm to retrieve essential items like medicine or snacks[cite: 1, 2].

## 📺 Project Demonstration
![Project Demo](media/project_video.gif) 
*(Note: If you have a .mp4 file, you can link it here or convert a highlight clip to a GIF for instant viewing.)*

## 📖 Project Description
This system bridges the gap in autonomy for patients with conditions such as paralysis or muscular dystrophy[cite: 1, 2]. It uses **Speech Recognition** to process verbal requests, which are then translated into specific coordinate movements for a multi-axis robotic arm[cite: 1, 2].

**Key Features:**
*   **Voice-Driven Interface:** Interprets keywords like "medicine" or "biscuit" to trigger automated routines[cite: 1, 2].
*   **Precision Manipulator:** Uses high-torque servos to securely grasp and deliver items[cite: 1, 2].
*   **Smooth Motion Logic:** Implements specialized algorithms to ensure gentle handling of fragile items[cite: 2].

---

## 🛠 Hardware Architecture
The system is built on an **Arduino Mega 2560** paired with a **PCA9685 PWM Driver** to handle high-current demands[cite: 1, 2].

*   **Microcontroller:** Arduino Mega 2560[cite: 1, 2].
*   **Servo Driver:** PCA9685 16-Channel 12-bit PWM Controller[cite: 1, 2].
*   **Actuators:** 
    *   3x **MG996R Servos** (Base, Shoulder, Forearm)[cite: 1, 2].
    *   1x **MG90S Servo** (Gripper)[cite: 1, 2].
*   **Power:** External 5V 10A DC Power Supply (Required for MG996R high torque)[cite: 1, 2].

### 🔌 Circuit Diagram
Refer to the detailed wiring schematic in the `hardware circuit` folder:
![Circuit Diagram](media/circuit_image.jpg)

---

## 🚀 Installation & Setup

### 1. Firmware (Arduino)
1.  Navigate to the `robotic_arm_control.ino` folder.
2.  Open the `.ino` file in the Arduino IDE[cite: 2].
3.  Install the **Adafruit PWM Servo Driver** library[cite: 1, 2].
4.  Upload the code to your Arduino Mega[cite: 2].

### 2. Software (Python)
1.  Ensure Python 3.x is installed on your laptop[cite: 1, 2].
2.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Update the `COM` port in `voice_control.py` to match your Arduino connection[cite: 1, 2].
4.  Run the application:
    ```bash
    python voice_control.py
    ```

---

## 🎮 Usage
1.  Place the **Medicine** at the $20^\circ$ position and the **Biscuit** at the $50^\circ$ position[cite: 2].
2.  Launch the Python GUI and click **START LISTENING**[cite: 1, 2].
3.  Speak clearly: *"Give me the medicine"* or *"Get the biscuit"*[cite: 1, 2].
4.  The arm will automatically pick up the item and deliver it to the designated delivery zone ($150^\circ$) before returning home[cite: 2].

---

## 📂 Repository Structure
*   `hardware circuit/`: Contains the electrical schematic[cite: 1, 2].
*   `media/`: Project demonstration video and images[cite: 1].
*   `robotic_arm_control.ino/`: Arduino firmware for servo kinematics[cite: 2].
*   `voice_control.py/`: Python GUI and speech recognition engine[cite: 1, 2].
*   `requirements.txt`: Python library dependencies[cite: 2].
