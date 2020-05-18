#!/usr/bin/env python3

import random
import argparse
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def roll(sides):
    return random.randint(1, sides)

def clicked(combo, spin):
    sides = combo.get()
    times = int(spin.get())

    result = 0
    count = times

    while(count != 0):
        result += roll(int(sides))
        count = count - 1

    messagebox.showinfo('Dice Roll Results', 'A D' + sides + ' was rolled ' + str(times) + ' times with a result of ' + str(result))

def cmdcall(sides, times):
    count = times
    result = 0

    while(count != 0):
        result += roll(sides)
        count = count - 1

    print()
    print()
    print(result)
    print()
    print()

def guicall():
    window = Tk()

    window.title("Dice Roller")

    window.geometry('350x80')

    sideslabel = Label(window, text="Number of Sides: ")

    sideslabel.grid(column=0, row=0)

    combo = Combobox(window)

    combo['values']= (4, 6, 8, 10, 12, 20, 100)

    combo.current(5) #set the selected item

    combo.grid(column=1, row=0)

    timeslabel = Label(window, text="Number of times to be rolled: ")

    timeslabel.grid(column=0, row=1)

    spininitvalue = IntVar()

    spininitvalue.set(1)

    spin = Spinbox(window, from_=1, to=10, width=1, textvariable=spininitvalue)

    spin.grid(column=1,row=1)

    btn = Button(window, text="Roll Dice", command=lambda: clicked(combo, spin))

    btn.grid(column=1, row=2)

    window.mainloop()


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sides', default=20, choices=[4, 6, 8, 10, 12, 20, 100], type=int, help="Number of sides on the dice to be rolled")
parser.add_argument('-t', '--times', default=1, type=int, help="Number of dice to be rolled")
parser.add_argument('-g', '--gui', action='store_true')
args = parser.parse_args()

gui_flag = args.gui
sides = args.sides
times = args.times

if (gui_flag):
    guicall()
else:
    cmdcall(sides, times)
    
