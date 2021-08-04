from datetime import datetime
from paho.mqtt import client as mqtt_client

broker = "192.168.0.128"  # insert your Broker ID
port = 1883
topic = "test"  # insert your topic

# username = ""
# password = ""


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("Connected to Broker."
              " Connection Result: " + str(rc) + " " + datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f"))

    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        message = msg.payload.decode('utf-8')
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f") + " --> " + message)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
