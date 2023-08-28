from pyautogui import *
from pynput import keyboard
import pyautogui
import time
#import keyboard
import numpy as np
import random
import win32api, win32con

time.sleep(2);
#monitor [wcoord, acoord, scoord, dcoord, 1coord, 2coord, 3coord, 4coord, 5coord]
#firmonitor = []
secmonitor = [(-1200, 660), (-1290, 720), (-1200, 780), (-1110, 720), (-350, 790), (-350, 690), (-300, 590), (-210, 520), (-70, 470)]

def click(x, press):
    win32api.SetCursorPos(x)
    if press:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def on_press(key):
    global press
    if key.char == 'w':
        i = 0
    elif key.char == 'a':
        i = 1
    elif key.char == 's':
        i = 2
    elif key.char == 'd':
        i = 3
    click(secmonitor[i], True)


def on_release(key):
    click(pyautogui.position(), False)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
#pyautogui.position()

#pyautogui.keyDown('w')
#time.sleep(0.1)
#pyautogui.keyUp('w')

#keyboard.on_press
