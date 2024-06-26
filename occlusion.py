import tkinter as tk
import keyboard
import time
import argparse
from threading import Timer

parser = argparse.ArgumentParser(description=" ")
parser.add_argument('-t', type=float, default=0.5000, help="Occolusion Time")
parser.add_argument('-s', type=int, default=1, help="Mode(Stackable or not)")
parser.add_argument('-a', type=int, default=1, help="Mode(Adaptive or not)")
args = parser.parse_args()
pre_duration = args.t
if_stackable = args.s
if_adaptive = args.a
print(args.a)
print(args.s)
print(args.t)
# change path here
PATH_BASE = "C:\\Users\\chenww\\Desktop\\"
PATH_STACKTABLE_AND_ADPATIVE = PATH_BASE + "out_python_stackable_and_adaptive.txt"
PATH_STACKTABLE_AND_NONADPATIVE = PATH_BASE + "out_python_stackable_and_nonadaptive.txt"
PATH_NONSTACKTABLE_AND_ADPATIVE = PATH_BASE + "out_python_nonstackable_and_adaptive.txt"
PATH_NONSTACKTABLE_AND_NONADPATIVE = PATH_BASE + "out_python_nonstackable_and_nonadaptive.txt"
PATH = None

if if_adaptive and if_stackable:
    PATH = PATH_STACKTABLE_AND_ADPATIVE

if if_adaptive and (not if_stackable):
    PATH = PATH_NONSTACKTABLE_AND_ADPATIVE 

if (not if_adaptive) and if_stackable:
    PATH = PATH_STACKTABLE_AND_NONADPATIVE

if (not if_adaptive) and (not if_stackable):
    PATH = PATH_NONSTACKTABLE_AND_NONADPATIVE

print(PATH)

f = open(PATH, 'w')
count = 1
timer = None
start = None
end = 0
left_time = args.t
nextduration = args.t
start_of_sequence = start
count_acc = 1


def create_black_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    return root

def turn_black_non_stackable():
    global end, start, count, pre_duration, if_adaptive
    end = time.time()
    if if_adaptive:
        pre_duration = pre_duration - (end - start - args.t)
    
    f.write(str(end - start) + "\n")
    print(count)
    count += 1
    black_screen.deiconify()

def turn_black_stackable():
    global end, start, count, pre_duration, left_time, nextduration, start_of_sequence, count_acc, timer, if_adaptive
    timer = None
    end = time.time()
    if if_adaptive:
        pre_duration = pre_duration - ((end - start_of_sequence)/count_acc - args.t)
    left_time = pre_duration
    f.write(str((end - start_of_sequence)/count_acc) + "\n")
    black_screen.deiconify()
    count_acc = 1

def on_key_event(event):
    global pre_duration, count, f, timer, start, end, left_time, nextduration, start_of_sequence, count_acc
    if event.name == 'space':
        if (not if_stackable):
            if timer:
                timer.cancel()
            black_screen.withdraw()  # Make screen visible when space is pressed
            timer = Timer(pre_duration, turn_black_non_stackable)
            start = time.time()
            timer.start()
        else: 
            if timer:
                timer.cancel()
                left_time = (left_time - (time.time() - start)) + pre_duration
                count_acc = count_acc + 1

            black_screen.withdraw()  # Make screen visible when space is pressed
            timer = Timer(left_time, turn_black_stackable)
            start = time.time()
            if count_acc == 1:
                start_of_sequence = time.time()
            timer.start()
            print(count)
            count += 1

    elif event.name == 'q':
        f.close()
        black_screen.destroy()
        keyboard.unhook_all()

black_screen = create_black_screen()
keyboard.on_press(on_key_event)
black_screen.mainloop()
