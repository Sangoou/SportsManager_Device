#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import threading

from data import game
from . import led
from . import button
from . import seven_segment

BLINK_TIME = 1

RIGHT_SCORE_BTN = 12
LEFT_SCORE_BTN = 16

RIGHT_SCORE_LED = (10, 9, 11)
LEFT_SCORE_LED = (6, 5, 0)

SITUATION_SELECT_BTN = 21
SITUATION_SEND_BTN = 20
SITUATION_LED = (26, 19, 13)

SEVEN_SEGMENT_POSITION = (4, 3, 2, 24)
SEVEN_SEGMENT_SEGMENT = (17, 22, 8, 7, 1, 27, 25)

score_button = [None, None]  # 0: right(B), 1: left(A)
score_led = [
    [None, None, None],  # Right
    [None, None, None]  # Left
]

situation_button = [None, None]
situation_led = [None, None, None]

score_seven_segment = None


def gpio_init():
    GPIO.setmode(GPIO.BCM)
    score_button_init()
    seven_segment_init()
    score_led_init()


def gpio_run():
    # score button
    global score_button
    score_button[0].start()
    score_button[1].start()

    # score seven segment
    global score_seven_segment
    score_seven_segment.start()

    # set score LED
    set_score_thread = threading.Thread(target=score_led_run)
    set_score_thread.start()
    pass


def score_button_init():
    global score_button
    # right score button = B
    score_button[0] = button.Button(args=(RIGHT_SCORE_BTN,))

    print(score_button[0])

    def right_button_on(self):
        if self.is_on:
            if time.time() - self.on_time >= 3 and self.on_time > 0:
                game.Game.score_decrease('B')
                self.on_time = -1
                # TODO MQTT -> score send
        else:
            self.on_time = time.time()

    def right_button_off(self):
        if time.time() - self.on_time < 3 and self.on_time > 0:
            game.Game.score_increase('B')
            # TODO MQTT -> score send

    score_button[0].set_on(right_button_on)
    score_button[0].set_off(right_button_off)

    # left score button = A
    score_button[1] = button.Button(args=(LEFT_SCORE_BTN,))

    def left_button_on(self):
        if self.is_on:
            if time.time() - self.on_time >= 3 and self.on_time > 0:
                game.Game.score_decrease('A')
                self.on_time = -1
                # TODO MQTT -> score send
        else:
            self.on_time = time.time()

    def left_button_off(self):
        if time.time() - self.on_time < 3 and self.on_time > 0:
            game.Game.score_increase('A')
            # TODO MQTT -> score send

    score_button[1].set_on(left_button_on)
    score_button[1].set_off(left_button_off)


def score_led_init():
    global score_led
    for i in range(3):
        score_led[0][i] = led.LED(args=(RIGHT_SCORE_LED[i],))
        score_led[1][i] = led.LED(args=(LEFT_SCORE_LED[i],))
        score_led[0][i].set_off()
        score_led[1][i].set_off()


def seven_segment_init():
    global score_seven_segment

    score_seven_segment = seven_segment.SevenSegment4(args=(
        SEVEN_SEGMENT_SEGMENT[0],
        SEVEN_SEGMENT_SEGMENT[1],
        SEVEN_SEGMENT_SEGMENT[2],
        SEVEN_SEGMENT_SEGMENT[3],
        SEVEN_SEGMENT_SEGMENT[4],
        SEVEN_SEGMENT_SEGMENT[5],
        SEVEN_SEGMENT_SEGMENT[6],
        SEVEN_SEGMENT_POSITION[0],
        SEVEN_SEGMENT_POSITION[1],
        SEVEN_SEGMENT_POSITION[2],
        SEVEN_SEGMENT_POSITION[3]
    )
    )


def situation_button_init():
    # TODO
    pass


def situation_led_init():
    # TODO
    pass


def score_led_run():
    global score_led
    for i in range(3):
        score_led[0][i].start()
        score_led[1][i].start()
    set_score_a = 0
    set_score_b = 0
    while True:
        time.sleep(0.5)
        set_score = game.Game.get_set_score()
        if set_score_a != set_score['A']:
            score_led[1][set_score_a].set_blink()
            time.sleep(BLINK_TIME)
            score_led[1][set_score_a].set_on()
            set_score_a = set_score['A']

        if set_score_b != set_score['B']:
            score_led[0][set_score_b].set_blink()
            time.sleep(BLINK_TIME)
            score_led[0][set_score_b].set_on()
            set_score_b = set_score['B']
