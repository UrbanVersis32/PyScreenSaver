# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from random import *

# Loop
def loop():
	turtle.title("Infinite Turtles Screen Saver")
	turtle.bgcolor("black")
	loop = 0
	repeat = 0
	# Create turtle colors
	if colorin.get() == "Green":
		color = "green"
	if colorin.get() == "White":
		color = "white"
	print("Selected Color: " + color)
	def move(turtlename):
		turtlename.forward(randint(1, 500))
		turtlename.right(randint(1, 359))
		turtlename.forward(randint(1, 500))
		turtlename.backward(randint(1, 500))
	while True: # move turtles around an generate them
		t1 = turtle.Turtle()
		t1.shape("turtle")
		t1.speed(int(speed.get()))
		t1.color(color)
		t1.penup()
		move(t1)
		repeat += 1
		print("Repeat", repeat)
		loop += 1
		print("Loop", loop)

# Initialize Tkinter Window
def screensaver():
	global colorin, speed
	def close():
		tk.destroy()
		turtle.bye()
		print("Closed Window")
	tk = Tk()
	tk.title("Spinning Turtles Screen Saver Interface")
	title = Label(tk, text = "Spinning Turtles Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)
	
	colortxt = Label(tk, text = "Color: ", font = ("Arial", 20))
	colortxt.grid(column = 0, row = 3)
	colorin = Combobox(tk)
	colorin["values"]= ("Green", "White")
	colorin.current(0)
	colorin.grid(column = 0, row = 4)
	
	speedtxt = Label(tk, text = "Speed: ", font = ("Arial", 20))
	speedtxt.grid(column = 0, row = 5)
	speed = Spinbox(tk, from_=1, to=100, width = 16)
	speed.grid(column = 0, row = 6)
	
	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 7, pady = 10)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 8, pady = 10)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 9)

	tk.mainloop()

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
