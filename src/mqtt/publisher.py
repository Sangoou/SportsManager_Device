#!/usr/bin/env python
import paho.mqtt.client as mqtt


# MQTT publisher
class Publisher:
    __topic = ""
    __broker_ip = '0.0.0.0'
    __broker_port = 1883
    __client = None

    def __init__(self, ip, port='1883', topic=""):
        self.__broker_ip = ip
        self.__broker_port = port
        self.__topic = topic
        self.__client = mqtt.Client()
        self.__client.connect(self.__broker_ip, self.__broker_port)

    def set_topic(self, topic):
        self.__topic = topic

    def publish(self, msg):
        self.__client.publish(self.__topic, msg)
        # timeout 2 sec
        self.__client.loop(2)
