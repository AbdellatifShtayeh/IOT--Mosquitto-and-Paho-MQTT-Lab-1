import paho.mqtt.client as mqtt
import time
import random


broker_address = "localhost"
broker_port = 1883
topic = "sensors/temperature"
My_ID = "12220214"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Failed to connect, return code {rc}\n")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "TemperaturePublisher")
client.on_connect = on_connect


client.connect(broker_address, broker_port)

client.loop_start()

try:
    while True:
        temperature = round(random.uniform(20.0, 25.0), 2)
        message = f"My ID: {My_ID}, Temperature: {temperature}°C"
        result = client.publish(topic, message)
        #result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Publishing stopped.")
    client.loop_stop()
    client.disconnect()