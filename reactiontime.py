
from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

# Start of code



# Click Function
def click(x,y): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# Main Code

while not keyboard.is_pressed('q'): 
    
    if pyautogui.pixel(1420, 400)[1] == 219: 
        click(1420, 400)

quit() 
