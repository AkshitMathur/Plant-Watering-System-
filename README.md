<h1>Plant Watering System</h1>
<hr>
<p>This is a simple project which involves watering plants without any huamn intervention.</p>

---

# 🌱 Automatic Plant Watering System using Arduino

This project is an **Arduino-based automatic plant watering system** that detects soil moisture levels and controls a water pump accordingly. It ensures that plants get the right amount of water without overwatering or underwatering.

---

## 🚀 Features

* 🌡️ **Soil Moisture Sensing** – Detects real-time soil dryness.
* 💧 **Automatic Watering** – Activates the pump when soil is dry.
* 🔌 **Low Power** – Consumes very little electricity.
* 🛠️ **Customizable** – Threshold values can be set in the Arduino code.
* 🌍 **Eco-Friendly** – Saves water and reduces human effort.

---

## 🖥️ Components Used

* Arduino Uno / Nano / Mega
* Soil Moisture Sensor
* Relay Module
* Mini Water Pump (5V/12V)
* Jumper Wires
* Power Supply
* Plant Pot with Soil

---

## ⚡ Circuit Diagram

* Soil Moisture Sensor → Arduino Analog Pin (e.g., A0)
* Relay Module → Arduino Digital Pin (e.g., D7)
* Pump → Relay → External Power Source
* Common GND for Arduino and Relay

---

## 📜 Working Principle

1. The soil moisture sensor continuously measures the soil’s water content.
2. If the moisture level is **below the threshold**, the Arduino triggers the **relay**, turning ON the pump.
3. Once the soil is sufficiently wet (above threshold), the pump turns OFF automatically.

---

## 📈 Future Improvements

* Add an **LCD display** to show soil moisture levels.
* Integrate with **IoT (Blynk / MQTT / Thingspeak)** for remote monitoring.
* Solar-powered operation for sustainability.

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repo, open issues, and submit pull requests.


