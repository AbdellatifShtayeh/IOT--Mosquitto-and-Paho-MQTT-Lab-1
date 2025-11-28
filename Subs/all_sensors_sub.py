import paho.mqtt.client as mqtt

broker_address = "localhost"
broker_port = 1883
topic = "sensors/#"  #subscribe to all topics under sensors/

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}\n")

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "AllSensorsSubscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port)

#handles reconnecting
client.loop_forever()