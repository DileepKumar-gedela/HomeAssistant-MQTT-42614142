# Home Assistant MQTT Sensor Integration – Assignment

**Student Name:** Gedela Dileep Kumar  
**Register Number:** 42614142  
**Course:** Internet of Things  
**Project:** MQTT Based Sensor Data Publishing and Home Assistant Visualization  

---

## 📌 Project Overview

This project demonstrates how to publish sensor values using **MQTT** and visualize them on **Home Assistant**. A Python script running on the host machine publishes data (Temperature, Humidity, and Light values) to an MQTT broker configured inside Home Assistant.

The published values are displayed as live sensors on the Home Assistant dashboard.

---

## 🏗 System Architecture
Python Script → MQTT Broker → Home Assistant Sensors → Dashboard

---

## 🛠 Requirements

- Home Assistant OS (Running in VirtualBox)
- Mosquitto MQTT Broker Add-on
- MQTT Integration enabled in Home Assistant
- Windows Host Machine (for running Python)
- Python 3.x installed
- `paho-mqtt` library installed

Install the MQTT library using:

```bash
pip install paho-mqtt

