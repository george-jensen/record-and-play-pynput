from pynput import mouse
import time
import json
import sys

n = len(sys.argv)

if n < 2:
    exit("Takes an argument - name of recording")

if n > 2:
    exit("Only takes one argument - name of recording")

if n == 2:
    name_of_recording = str(sys.argv[1])

print("Scroll to end the recording")
storage = []
count = 0

def on_move(x, y):
    if len(storage) >= 1:
        if storage[-1]['action'] == "pressed" or (storage[-1]['action'] == "moved" and time.time() - storage[-1]['_time'] > 0.01):
            json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
            storage.append(json_object)

def on_click(x, y, button, pressed):
    json_object = {'action':'pressed' if pressed else 'released', 'button':str(button), 'x':x, 'y':y, '_time':time.time()}
    storage.append(json_object)

def on_scroll(x, y, dx, dy):
    print("Cancelling")
    with open('data/{}.txt'.format(name_of_recording), 'w') as outfile:
        json.dump(storage, outfile)
    return False

# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
        on_move=on_move) as listener:
    listener.join()