#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Start of Program
from gpio import gpio_main
from qr import reader



# TODO GPIO
gpio_main.gpio_init()
gpio_main.gpio_run()
# TODO 변수 초기화
# TODO QR
reader.read_qr_code()
# TODO MQTT sub
# TODO MQTT pub
