import pyautogui
import time

is_active = True
clicks_per_sond = float(input("How many clicks per second?"))

for i in range(5):
    print(5-i)
    time.sleep(1)


time_per_click = 1/clicks_per_sond
while is_active:
    x, y = pyautogui.position()

    if x < 10 and y < 10:
        break

    pyautogui.click()
    time.sleep(time_per_click)
