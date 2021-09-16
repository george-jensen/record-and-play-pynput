from pynput import mouse
from datetime import datetime as time

storage = []

def on_click(x, y, button, pressed):
    print('{0} at {1} - Time: {2}'.format(
        'Pressed' if pressed else 'Released',
        (x, y), time.now()))
    json_object = {'x':x, 'y':y,'time':time.now()}
    storage.append(json_object)
    if len(storage) > 2:
        print(storage[-1]['time'] - storage[-2]['time'])

def on_scroll(x, y, dx, dy):
    print("Cancelling")
    return False

# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
