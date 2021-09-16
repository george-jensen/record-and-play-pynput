from pynput.mouse import Button, Controller
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

mouse = Controller()

for loop in range(number_of_plays):
    for index, obj in enumerate(data):
        action, x, y, _time= obj['action'], obj['x'], obj['y'], obj['_time']
        try:
            next_movement = data[index+1]['_time']
            pause_time = next_movement - _time
        except IndexError as e:
            pause_time = 1
        
        print("x: {0}, y: {1}, action: {2}, time: {3}".format(x, y, action, _time))
        mouse.position = (x, y)
        if action == "pressed" or action == "released":
            time.sleep(0.1)
        if action == "pressed":
            mouse.press(Button.left if obj['button'] == "Button.left" else Button.right)
        elif action == "released":
            mouse.release(Button.left if obj['button'] == "Button.left" else Button.right)
        time.sleep(pause_time)



