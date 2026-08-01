import tkinter as tk
import threading
import autoclicker
import time

is_active = False
button_pause_text = "Start"


def pause_or_continue():
    global is_active
    global clicks_per_second

    clicks_per_second = scale.get()

    if is_active:
        is_active = False
        autoclicker.stop = True
        pause_button.config(text="Continue")
    else:
        is_active = True
        autoclicker.stop = False
        pause_button.config(text="Pause")
        threading.Thread(target=countdown, daemon=True).start()


def run_autoclicker(clicks_per_second):
    threading.Thread(target=autoclicker.auto_clicking,
                     args=(clicks_per_second,), daemon=True).start()


def countdown():
    for i in range(6):
        countdown_label.config(text=5-i)
        time.sleep(1)
    run_autoclicker(clicks_per_second)


window = tk.Tk()
window.title("Autoclicker")
window.geometry("200x300")

scale = tk.Scale(window, from_=0.1, to=10.0,
                 resolution=0.1, orient="horizontal")
scale.pack()

pause_button = tk.Button(window, text="Start",
                         command=pause_or_continue)
pause_button.pack()

countdown_label = tk.Label(window, text="")
countdown_label.pack()

window.mainloop()
