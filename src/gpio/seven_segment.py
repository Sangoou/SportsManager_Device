#!/usr/bin/env python


import RPi.GPIO as GPIO
from time import sleep
import threading

from data import game

FRAME_TIME = 5 * 0.001

NUMBER = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 0, 0, 1, 1)  # 9
)


class SevenSegment4(threading.Thread):
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.__segment = args[:7]
        self.__position = args[7:]
        self.__number = [0, 0, 0, 0]

        for seg in range(7):
            GPIO.setup(self.__segment[seg], GPIO.OUT)
        for pos in range(4):
            GPIO.setup(self.__position[pos], GPIO.OUT)

    def run(self):
        count = 0
        while True:
            count = count + 1
            score = game.Game.get_score()
            self.__number[0] = int(score['A'] / 10)
            self.__number[1] = score['A'] % 10
            self.__number[2] = int(score['B'] / 10)
            self.__number[3] = score['B'] % 10
            for i in range(4):
                for pos in range(4):
                    if i == pos:
                        GPIO.output(self.__position[pos], False)
                    else:
                        GPIO.output(self.__position[pos], True)
                for j in range(7):
                    if NUMBER[self.__number[i]][j] == 0:
                        GPIO.output(self.__segment[j], False)
                    else:
                        GPIO.output(self.__segment[j], True)
                sleep(FRAME_TIME)

            if game.Game.is_end() and count > 20:
                for i in range(4):
                    GPIO.output(self.__position[i], True)
                count = 0
                sleep(0.3)
