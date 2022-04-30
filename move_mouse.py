import pyautogui as pg
from pynput.mouse import Listener as MouseListener
import time
import mouse



print("Middle mouse button to enable\nto quit\n")
x1 = float(input("Input Speed (in seconds) eg 0.1: ")) 
y1 = float(input("input number of pixel you want to move: ")) 

pressTime = 0
releaseTime = 0
total_time = 0
enable = False

def on_click(x,y,button,pressed):
    global pressTime, releaseTime, total_time, enable
    btn = button.name
    if btn == 'x1':
        mouse_listener.stop()
    if btn == 'x2':
        print("Disabled")
        enable = False
    if btn == 'middle':
        print("Enabled")
        enable = True
    if pressed:
        pressTime = time.time()
        
    if not pressed:
        releaseTime = time.time()
        total_time = releaseTime-pressTime
        x , y = pg.position()
        if enable and total_time > 0.2 and btn == 'left':
            mouse.move(x, y+y1, duration=x1) 
        print("Time:" ,total_time)
        return True

mouse_listener = MouseListener(on_click=on_click)

mouse_listener.start()
mouse_listener.join()



