#!/usr/bin/env python

from gpio import gpio_main
from mqtt import subscriber
from mqtt import publisher
from data import game

from time import sleep
import ast
from PIL import Image
from pyzbar.pyzbar import decode

from picamera import PiCamera
from uuid import getnode as get_mac

SERVER_IP = "221.147.113.235"
SERVER_PORT = 5415


def read_qr_code():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    i = 0
    while True:
        # Capture Image
        sleep(1)
        camera.capture('./capture' + str(i) + '.jpg')

        # Read QR from Image
        result = decode(Image.open('./capture' + str(i) + '.jpg'))
        i = i + 1
        print("QR Decode Content: " + str(result))
        if result:
            id = str(result[0].data)
            print("QR Code Content: " + id)
            mac = get_mac()
            gpio_main.mqtt_pub = publisher.Publisher(SERVER_IP, SERVER_PORT, '/event/' + mac)
            gpio_main.mqtt_sub = subscriber.Subcriber(SERVER_IP, SERVER_PORT, '/sm/' + id + '/' + mac)
            gpio_main.mqtt_sub_all = subscriber.Subcriber(SERVER_IP, SERVER_PORT, '/sm/' + id)
            pub = publisher.Publisher(SERVER_IP, SERVER_PORT, '/connect')
            pub.publish(mac)

            # 제어
            def device_control(client, userdata, msg):
                data = ast.literal_eval(msg.payload)
                command = data['command']
                if command == 0:
                    pass
                elif command == 1:
                    pass
                elif command == 2:
                    pass
                elif command == 3:
                    info = data['content']
                    game.Game.game_init()
                    game.Game.set_id(info['id'])
                    game.Game.set_team_id('A', info['teamA'])
                    game.Game.set_team_id('B', info['teamB'])
                    game.Game.set_win_score(info['scoreToWin'])
                    game.Game.set_win_set_score(info['setToWIn'])
                    pass
                elif command == 4:
                    pass
                else:
                    print("Invalid Data: " + str(data))
            gpio_main.mqtt_sub.set_on_message(device_control)
            gpio_main.mqtt_sub_all.set_on_message(device_control)

            break
    camera.stop_preview()
