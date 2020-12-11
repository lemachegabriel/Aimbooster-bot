from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import random 

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#this is the center color of the target in the game: (255, 219, 195)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(371,270,600,420)) #this region is on my computer on your computer can be different
                                    
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+371,y+270)
                time.sleep(0.05)
                break
