from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time
import json
import sys

n = len(sys.argv)

if n < 3:
    exit("Takes two arguments - name of recording to play and number of times to play it")

if n > 3:
    exit("Only takes two argument - name of recording to play and number of times to play it")

if n == 3:
    name_of_recording = "data/" + str(sys.argv[1]) +'.txt'
    number_of_plays = int(sys.argv[2])

with open(name_of_recording) as json_file:
    data = json.load(json_file)

special_keys = {"Key.shift": Key.shift, "Key.tab": Key.tab, "Key.caps_lock": Key.caps_lock, "Key.ctrl": Key.ctrl, "Key.alt": Key.alt, "Key.cmd": Key.cmd, "Key.cmd_r": Key.cmd_r, "Key.alt_r": Key.alt_r, "Key.ctrl_r": Key.ctrl_r, "Key.shift_r": Key.shift_r, "Key.enter": Key.enter, "Key.backspace": Key.backspace, "Key.f19": Key.f19, "Key.f18": Key.f18, "Key.f17": Key.f17, "Key.f16": Key.f16, "Key.f15": Key.f15, "Key.f14": Key.f14, "Key.f13": Key.f13, "Key.media_volume_up": Key.media_volume_up, "Key.media_volume_down": Key.media_volume_down, "Key.media_volume_mute": Key.media_volume_mute, "Key.media_play_pause": Key.media_play_pause, "Key.f6": Key.f6, "Key.f5": Key.f5, "Key.right": Key.right, "Key.down": Key.down, "Key.left": Key.left, "Key.up": Key.up, "Key.page_up": Key.page_up, "Key.page_down": Key.page_down, "Key.home": Key.home, "Key.end": Key.end, "Key.delete": Key.delete, "Key.space": Key.space}

mouse = MouseController()
keyboard = KeyboardController()

for loop in range(number_of_plays):
    for index, obj in enumerate(data):
        action, _time= obj['action'], obj['_time']
        try:
            next_movement = data[index+1]['_time']
            pause_time = next_movement - _time
        except IndexError as e:
            pause_time = 1
        
        if action == "pressed_key" or action == "released_key":
            key = obj['key'] if 'Key.' not in obj['key'] else special_keys[obj['key']]
            print("action: {0}, time: {1}, key: {2}".format(action, _time, str(key)))
            if action == "pressed_key":
                keyboard.press(key)
            else:
                keyboard.release(key)
            time.sleep(pause_time)


        else:
            x, y = obj['x'], obj['y']
            print("x: {0}, y: {1}, action: {2}, time: {3}".format(x, y, action, _time))
            mouse.position = (obj['x'], y)
            if action == "pressed" or action == "released":
                time.sleep(0.1)
            if action == "pressed":
                mouse.press(Button.left if obj['button'] == "Button.left" else Button.right)
            elif action == "released":
                mouse.release(Button.left if obj['button'] == "Button.left" else Button.right)
            time.sleep(pause_time)
    


