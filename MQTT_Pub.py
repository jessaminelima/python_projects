from datetime import datetime
from paho.mqtt import client as mqtt_client

import time

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


def publish(client):

    while True:
        time.sleep(1)
        # text = input("Message to send:\n")
        # msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f") + " --> " + text
        msg = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f") + " --> " + "Testing"

        client.publish(topic, msg)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
