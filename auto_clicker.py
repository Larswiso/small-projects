# pip install pyautogui, keyboard

import time
import pyautogui
import keyboard
 
# interval in seconds 
interval = 1

# time before auto clicker starts
time.sleep(6)

while True:

    time.sleep(interval) 
    
    pyautogui.click()
    print("Clicked!")

    # to exit the auto clicker: spam "q"
    if keyboard.is_pressed("q") == True:
        quit()