from pynput import keyboard, mouse
import time
import json
import paho.mqtt.publish as publish

BROKER = "broker.hivemq.com"
TOPIC = "study/tracker"

last_activity = time.time()

def on_activity(*args):
    global last_activity
    last_activity = time.time()

keyboard.Listener(on_press=on_activity).start()
mouse.Listener(on_move=on_activity).start()

while True:
    if time.time() - last_activity < 60:
        status = "focused"
    else:
        status = "distracted"

    data = {
        "status": status,
        "timestamp": time.time()
    }

    publish.single(TOPIC, json.dumps(data), hostname=BROKER)
    print(data)

    time.sleep(5)