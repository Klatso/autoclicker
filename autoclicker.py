import pyautogui
import time

stop = False


def auto_clicking(clicks_per_second):
    time_per_click = 1/clicks_per_second
    while True:
        x, y = pyautogui.position()

        if x < 10 and y < 10 or stop == True:
            break

        pyautogui.click()
        time.sleep(time_per_click)
