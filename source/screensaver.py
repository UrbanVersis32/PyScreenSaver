# Screen Saver Program

# Python Version Validation
import sys

print("Python Version: " + sys.version)

check = sys.version[0:1] # Trim system version string so that the variable is a string of only "2" or "3"

if check == "3": # Correct Python version
	pass
	
else: # Outdated Python Version (Version 2)
	print("\nYour Python Version is Outdated.")
	sys.exit()

# Continue code
import turtle
# Lines 19-22 are imported on all screen savers to build Tkinter window
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
# Import the run functions from the screen saver files
from hexagonal import screensaver as ss1
from growing import screensaver as ss2
from turtles import screensaver as ss3
from matrix import screensaver as ss4
from circular import screensaver as ss5
from magiclight import screensaver as ss6
from clock import screensaver as ss7

print("\nWelcome to the Screen Saver Program!")
print("Running Screensaver...")

def closewindow():
	tk.destroy()
	turtle.bye()
	print("Closed Window")
	sys.exit()

def info():
	print("Showing Info")
	messagebox.showinfo("About Screen Saver", "PyScreenSaver v0.1.0; Python Version:" + sys.version)
	
# Create Tkinter window

tk = Tk()
tk.title("PyScreenSaver")
title = Label(tk, text = "PyScreenSaver Dashboard", font = ("Verdana", 40))
title.grid(column = 0, row = 0)

# Add menus at top of screen
menu = Menu(tk)
data = Menu(menu, tearoff = 0)
data.add_command(label='Help', command=info)
menu.add_cascade(label='Info', menu=data)

title = Label(tk, text = "Click on any of the buttons below to access a screen saver.", font = ("Verdana", 18))
title.grid(column = 0, row = 1)

sc1 = Button(tk, text = "Hexagonal", command = ss1)
sc1.grid(column = 0, row = 2, pady = 5)

sc2 = Button(tk, text = "Growing", command = ss2)
sc2.grid(column = 0, row = 3, pady = 5)

sc3 = Button(tk, text = "Spinning Turtles", command = ss3)
sc3.grid(column = 0, row = 4, pady = 5)

sc4 = Button(tk, text = "The Matrix", command = ss4)
sc4.grid(column = 0, row = 5, pady = 5)

sc5 = Button(tk, text = "Circular", command = ss5)
sc5.grid(column = 0, row = 6, pady = 5)

sc6 = Button(tk, text = "Magic Light", command = ss6)
sc6.grid(column = 0, row = 7, pady = 5)

sc7 = Button(tk, text = "Clock", command = ss7)
sc7.grid(column = 0, row = 8, pady = 5)

close = Button(tk, text = "Close", command = closewindow)
close.grid(column = 0, row = 9, pady = 10)

info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
info.grid(column = 0, row = 10)

tk.config(menu=menu)

tk.mainloop()
