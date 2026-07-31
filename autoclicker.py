
# nicht starten!!!

import pyautogui
import time

is_active = True
cps = float(input("How many clicks per second?"))
time_per_click = 1/cps

for i in range(5):
    print(5-i)
    i += 1
    time.sleep(1)

while is_active:
    x, y = pyautogui.position()

    if x < 10 and y < 10:
        break

    pyautogui.click()
    time.sleep(time_per_click)
