#!/usr/bin/env python


import RPi.GPIO as GPIO
from time import sleep
import threading

CHECK_TIME = 50 * 0.001


class Button(threading.Thread):
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.__pin_number = args[0]
        GPIO.setup(self.__pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        def default_function(): {}

        self.__on = default_function
        self.__off = default_function
        self.is_on = False

    def run(self):
        while True:
            sleep(CHECK_TIME)
            if GPIO.input(self.__pin_number):
                self.__on(self)
                self.is_on = True
            elif self.is_on:
                self.__off(self)
                self.is_on = False

    def set_on(self, func):
        self.__on = func

    def set_off(self, func):
        self.__off = func
