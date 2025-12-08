import time
import json
import paho.mqtt.client as mqtt
student_name = "Gedela Dileep Kumar"
unique_id = "42614142"
topic = "home/gedeladileep-2025/sensor"

broker_host = "192.168.1.12" 
broker_port = 1883
username = "dileep"          
password = "nLT5VXtx6RpizQm" 

def get_sensor_values():
    """
    Fake sensor values.
    These are the values you are publishing to Home Assistant.
    """
    temperature = 25          
    humidity = 60       
    light = 80  

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
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()

