from pynput import mouse
from pynput import keyboard
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

print("Scroll to end the recording for mouse, esc to end the recording for keyboard (both to finish recording)")
storage = []
count = 0

def on_press(key):
    try:
        json_object = {'action':'pressed_key', 'key':key.char, '_time': time.time()}
    except AttributeError:
        if key == keyboard.Key.esc:
            return False
        json_object = {'action':'pressed_key', 'key':str(key), '_time': time.time()}
    storage.append(json_object)

def on_release(key):
    try:
        json_object = {'action':'released_key', 'key':key.char, '_time': time.time()}
    except AttributeError:
        json_object = {'action':'released_key', 'key':str(key), '_time': time.time()}
    storage.append(json_object)
        

def on_move(x, y):
    if len(storage) >= 1:
        if storage[-1]['action'] == "pressed" or (storage[-1]['action'] == "moved" and time.time() - storage[-1]['_time'] > 0.02):
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


# Collect events from keyboard until esc
# Collect events from mouse until scroll
keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

mouse_listener = mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
        on_move=on_move)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
