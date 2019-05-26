#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import threading

BLINK_TIME = 100 * 0.001


class LED(threading.Thread):
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.__pin_number = args[0]
        self.__state = 'off'
        GPIO.setup(self.__pin_number, GPIO.OUT)

    def run(self):
        while True:
            if self.__state == 'off':
                self.off()
                sleep(BLINK_TIME)
            elif self.__state == 'on':
                self.on()
                sleep(BLINK_TIME)
            elif self.__state == 'blink':
                self.on()
                sleep(BLINK_TIME)
                self.off()
                sleep(BLINK_TIME)

    def on(self):
        if self.__pin_number:
            GPIO.output(self.__pin_number, True)

    def off(self):
        if self.__pin_number:
            GPIO.output(self.__pin_number, False)

    def set_on(self):
        self.__state = 'on'

    def set_off(self):
        self.__state = 'off'

    def set_blink(self):
        self.__state = 'blink'
