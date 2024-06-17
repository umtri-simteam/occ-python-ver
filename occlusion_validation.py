import tkinter as tk
import keyboard
import time
import argparse

parser = argparse.ArgumentParser(description=" ")
parser.add_argument('-t', type=float, default=0.5000, help="Occolusion Time")
args = parser.parse_args()
pre_duration = args.t

PATH = "C:\\Users\\chenww\\Desktop\\script_out.txt"

f = open(PATH, 'w')
count = 1

def create_black_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    return root

def show_screen_for_a_moment():
    global pre_duration
    black_screen.withdraw()
    start = time.time()
    time.sleep(pre_duration)
    black_screen.deiconify()
    end = time.time()
    return start, end

def on_key_event(event):
    global pre_duration
    global count
    global f
    if event.name == 'space':  
        start, end = show_screen_for_a_moment()
        pre_duration = pre_duration - (end - start - args.t)
        f.write(str(end - start) + "\n")
        print(count)
        count += 1
    elif event.name == 'q':
        f.close()  
        black_screen.destroy()
        keyboard.unhook_all()

black_screen = create_black_screen()

keyboard.on_press(on_key_event)

black_screen.mainloop()