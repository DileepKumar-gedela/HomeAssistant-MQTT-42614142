import time
import json
import paho.mqtt.client as mqtt

# ----- REQUIRED BY ASSIGNMENT -----
student_name = "Gedela Dileep Kumar"
unique_id = "42614142"
topic = "home/gedeladileep-2025/sensor"
# ----------------------------------

# MQTT broker details (Home Assistant VM)
broker_host = "192.168.1.12"   # IP of your Home Assistant VM
broker_port = 1883
username = "dileep"            # MQTT username you created
password = "nLT5VXtx6RpizQm"   # MQTT password you created

def get_sensor_values():
    """
    Fake sensor values.
    These are the values you are publishing to Home Assistant.
    """
    temperature = 25           # as required
    humidity = 60              # as required
    light = 80                 # extra sensor (any other name is also okay)

    return {
        "student_name": student_name,
        "unique_id": unique_id,
        "temperature": temperature,
        "humidity": humidity,
        "light": light
    }

def main():
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.connect(broker_host, broker_port, 60)

    try:
        while True:
            payload = get_sensor_values()
            json_payload = json.dumps(payload)
            print(f"Publishing to {topic}: {json_payload}")
            client.publish(topic, json_payload, qos=0, retain=True)
            time.sleep(5)  # publish every 5 seconds
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
