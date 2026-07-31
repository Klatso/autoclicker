import pyautogui
import time


is_active = True
cps = float(input("How many clicks per secound?"))
time_per_click = 1/cps

time.sleep(5)
while is_active:
    x, y = pyautogui.position()

    if x < 10 and y < 10:
        break

    pyautogui.click()
    time.sleep(time_per_click)
