#!/usr/bin/env python
import paho.mqtt.client as mqtt


# MQTT subscriber
class Subscriber:
    __topic = ""
    __broker_ip = '0.0.0.0'
    __broker_port = 1883
    __client = None

    def __init__(self, ip, port='1883', topic=""):
        self.__broker_ip = ip
        self.__broker_port = port
        self.__client = mqtt.Client()

        def on_connect(client, user_data, rc):
            print("Connect With Result Coe: " + str(rc))
            client.subscribe(topic)

        self.__client.on_connect = on_connect

    # on_message(client, user_data, msg)
    def set_on_message(self, on_message):
        self.__client.on_message = on_message

    def connect(self):
        self.__client.connect(self.__broker_ip, self.__broker_port)
        return self.__client

    def get_client(self):
        return self.__client
