# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from random import randint
from time import *

# Loop
def run():
	rand = randint(low, high)
	print(rand)
	textlabel = Label(matrix, text = rand, font = ("Courier", 12), foreground = "green", background = "black", anchor = N, width = 200)
	textlabel.pack()

def loop():
	global matrix
	# Simplify Variables
	low = int(rawlow.get())
	high = int(rawhigh.get())
	interval = int(rawinterval.get()) / 1000
	if high == 0: # Create Default value
		high = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 # Characters: 128
		
	print("Low Number:", low)
	print("High Number:", high)
	print("Interval:", interval)
	num = 3
	# 3-Second countdown so the user can read the above message
	for x in range(0, 3):
		print("Starting in", num)
		num -= 1
		sleep(1)
	
	while True: # Run this, except when run is False
		num = randint(low, high)
		print(num)
		sleep(interval)
		if run == False:
			break
		# We use the following code instead of tk.mainloop() to disable the code-stopping properties of tk.mainloop()
		tk.update_idletasks()
		tk.update()
		
# Initialize Tkinter Window
def screensaver():
	global rawlow, rawhigh, rawinterval, run, tk
	run = True
	def close():
		run = False
		tk.destroy()
		print("Exited Loop")
	tk = Tk()
	tk.title("Matrix Screen Saver Interface")
	title = Label(tk, text = "Matrix Screen Saver", font = ("Verdana", 30))
	title.grid(column = 0, row = 0)
	
	lowtxt = Label(tk, text = "Lowest Possible Number: ", font = ("Arial", 20))
	lowtxt.grid(column = 0, row = 1)
	rawlow = Spinbox(tk, from_=0, to=9, width = 64)
	rawlow.insert(END, 1)
	rawlow.grid(column = 0, row = 2)
	
	hightxt = Label(tk, text = "Highest Possible Number (Enter 0 for default): ", font = ("Arial", 20))
	hightxt.grid(column = 0, row = 3)
	rawhigh = Spinbox(tk, from_=0, to=9, width = 64)
	rawhigh.grid(column = 0, row = 4)
	
	intervaltxt = Label(tk, text = "Interval (In Milliseconds): ", font = ("Arial", 20))
	intervaltxt.grid(column = 0, row = 5)
	rawinterval = Spinbox(tk, from_=0, to=9, width = 16)
	rawinterval.grid(column = 0, row = 6)
	
	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 7, pady = 10)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 8, pady = 10)

	info = Label(tk, text = "By Urban Versis 32	Note: This Screen Saver runs in the black screen \n rather than opening up a new window", font = ("Arial", 10))
	info.grid(column = 0, row = 9)
	
	# No tk.mainloop() here; See line 42 for details

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
