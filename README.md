# Smart Waste Management & Automated Segregation System

## Overview
The **Smart Waste Management & Automated Segregation System** is an advanced IoT and AI-powered solution designed to efficiently monitor, classify, and manage waste. By integrating **ESP32, LoRa, GPS, ultrasonic sensors, Raspberry Pi, and machine learning**, this system ensures optimal waste classification and real-time tracking. It assists municipal corporations and households in managing waste through timely alerts and automated segregation.

## Features
- ✅ **Automated Waste Classification:** Uses **soil moisture sensors** for dry/wet classification and **machine learning** for organic/recyclable sorting.
- ✅ **Bin Fill Level Monitoring:** Ultrasonic sensors detect when a bin is **90% full** and trigger alerts.
- ✅ **Real-Time GPS Tracking:** NEO-6M GPS module provides **location data** for smart bins.
- ✅ **Long-Range Communication:** LoRa (SX1278) enables **data transmission** over long distances.
- ✅ **Solar-Powered System:** Uses **solar panels** and batteries for sustainable energy.
- ✅ **Mobile & Web Dashboard:** Sends **real-time alerts** to municipal authorities and household users.

## System Architecture
The system consists of **two main components**:

### 1️⃣ Smart Waste Management System (IoT-based)
- **ESP32 DevKit V1** (Microcontroller)
- **SX1278 LoRa Module** (Long-range communication)
- **HC-SR04 Ultrasonic Sensor** (Bin fill level detection)
- **Capacitive Soil Moisture Sensor** (Dry/Wet waste classification)
- **NEO-6M GPS Module** (Location tracking)
- **Solar Panel (6V, 5W) & 18650 Li-Ion Battery (3.7V, 5000mAh)** (Power System)
- **TP4056 Charging Module, MT3608 Boost Converter, AMS1117 Voltage Regulator**

### 2️⃣ Automated Waste Segregation System (AI & ML-based)
- **Arduino Uno R3 & Raspberry Pi 3** (Microcontrollers)
- **Ultrasonic Sensors (HC-SR04)** (Waste detection)
- **Camera Module (USB Webcam)** (Image-based classification)
- **Servo Motor (SG90)** (Sorting mechanism)
- **TensorFlow/Keras & Python** (Machine learning model for classification)

## How It Works
1. **Waste Detection:** Ultrasonic sensors detect the presence of waste.
2. **Waste Classification:**
   - **Dry/Wet Classification:** Soil moisture sensors analyze moisture content.
   - **Organic/Recyclable Sorting:** A camera module captures waste images, which are processed by a **machine learning model**.
3. **Sorting Mechanism:** A servo motor directs waste to the appropriate bin.
4. **Data Processing & Transmission:** ESP32 sends data via **LoRa** to a central monitoring system.
5. **GPS Tracking:** Bins' locations are updated in real-time.
6. **Alert System:**
   - If a bin reaches **90% capacity**, an alert is sent to municipal authorities.
   - Users receive notifications via the **mobile app/web dashboard** for timely collection.

## Performance & Accuracy
- 📏 **Ultrasonic Sensor Detection Accuracy:** **98%**
- 🎯 **Machine Learning Classification Accuracy:** **92%**
- ⚡ **Sorting Efficiency:** **High precision with minimal error**

## Comparison with Existing Solutions
| Feature | Bhopal | Mumbai | Pune | Our System |
|---------|--------|--------|------|------------|
| AI-Based Sorting | ✅ | ❌ | ✅ | ✅ |
| GPS Tracking | ✅ | ✅ | ✅ | ✅ |
| IoT-Based Sensors | ✅ | ✅ | ✅ | ✅ |
| Solar Power | ❌ | ❌ | ❌ | ✅ |
| LoRa Communication | ❌ | ❌ | ❌ | ✅ |

## Future Enhancements 🚀
- ✅ **Expand classification** to include more waste types.
- ✅ **Improve machine learning model** with a larger dataset.
- ✅ **Integrate cloud-based monitoring and analytics** for enhanced tracking.
- ✅ **Implement smart contracts using blockchain** for transparent waste management.

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/smart-waste-management.git
   ```
2. Install required libraries for ESP32:
   - `LoRa.h`
   - `TinyGPS++`
   - `ArduinoJson`
3. Install required Python dependencies for ML model:
   ```bash
   pip install tensorflow keras numpy opencv-python
   ```
4. Upload the ESP32 firmware using Arduino IDE or PlatformIO.
5. Set up the Raspberry Pi with the machine learning model.
6. Deploy the hardware in designated waste collection points.
7. Use the **mobile app/web dashboard** to monitor waste levels and receive alerts.

## Team Members 👨‍💻
- **Tirtha Shah** (22CE121)
- **Utsav Dholakiya** (22EC011)
- **Nitisha Thakor** (22EC061)
- **Om Savani** (22EC056)

### Supervisors
- **Prof. Jitendra Chaudhari**
- **Prof. Akshat Patel**

## References 📚
- **Ultrasonic Sensor Datasheet:** [HCSR04](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)
- **Servo Motor Datasheet:** [SG90](https://www.friendlywire.com/projects/ne555-servo-safe/SG90-datasheet.pdf)
- **Arduino Uno R3 Datasheet:** [A000066](https://datasheet.octopart.com/A000066-Arduino-datasheet-166248095.pdf)
- **Raspberry Pi 3 Datasheet:** [RS-Online](https://us.rs-online.com/m/d/4252b1ecd92888dbb9d8a39b536e7bf2.pdf)
- **Machine Learning Model Dataset:** [Mendeley Dataset](https://data.mendeley.com/datasets/n3gtgm9jxj/2)

## License 📜
This project is licensed under the **MIT License**.

---
💡 *If you find this project useful, feel free to ⭐ star the repository and contribute!* 🚀

