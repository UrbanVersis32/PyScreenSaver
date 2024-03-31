# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from random import *

# Loop
def loop():
	screen = turtle.Turtle()
	turtle.title("Growing Screen Saver")
	fullcolor = color.get()
	turtle.bgcolor("black")
	print("Selected Color: " + str(fullcolor))
	hex = 0
	loop = 1
	line = 0
	actualincrement = int(increment.get())
	completeshape = "classic"
	possiblecolors = ["red", "green", "blue"] # Create list of possible random colors
	while True: # This code is based upon the Hexagonal screen saver
		print("Loop", loop)
		if color.get().lower() == "random":
			fullcolor = choice(possiblecolors)
		
		if shape.get() == "No Shape":
			screen.hideturtle()
		else:
			completeshape = shape.get().lower()
			
		screen.shape(completeshape)
		if color.get().lower() == "random":
			fullcolor = choice(possiblecolors)
		screen.speed(int(speed.get()))
		for n in range(int(time.get())): # Draw Hexagons
			hex += 1
			print("Hexagon", hex)
			for i in range(6):
				line += 1
				print("Line", line)
				screen.color(fullcolor)
				screen.forward(actualincrement)
				screen.left(60)
			screen.right(10)
			actualincrement += int(increment.get())
			if actualincrement >= int(length.get()):
				screen.reset()
				hex = 0
				actualincrement = int(increment.get())
				print("Loop", loop)
				loop += 1
		screen.color('white')

# Initialize Tkinter Window
def screensaver():
	global color, speed, increment, time, length, shape
	def close():
		tk.destroy()
		turtle.bye()
		print("Closed Window")
	tk = Tk()
	tk.title("Growing Screen Saver Interface")
	title = Label(tk, text = "Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)

	colortxt = Label(tk, text = "Color (Enter random for random colors): ", font = ("Arial", 20))
	colortxt.grid(column = 0, row = 2)
	color = Entry(tk, width = 16)
	color.insert(END, "random")
	color.grid(column = 0, row = 3)

	speedtxt = Label(tk, text = "Speed: ", font = ("Arial", 20))
	speedtxt.grid(column = 0, row = 4)
	speed = Spinbox(tk, from_=4, to=100, width = 16)
	speed.grid(column = 0, row = 5)

	incrementtxt = Label(tk, text = "Increment: ", font = ("Arial", 20))
	incrementtxt.grid(column = 0, row = 6)
	increment = Spinbox(tk, from_=1, to=1000, width = 16)
	increment.grid(column = 0, row = 7)
	
	timetxt = Label(tk, text = "Time: ", font = ("Arial", 20))
	timetxt.grid(column = 0, row = 8)
	time = Spinbox(tk, from_=0, to=1000, width = 16)
	time.insert(END, 1)
	time.grid(column = 0, row = 9)

	lengthtxt = Label(tk, text = "Length: ", font = ("Arial", 20))
	lengthtxt.grid(column = 0, row = 10)
	length = Spinbox(tk, from_=0, to=1000, width = 16)
	length.insert(END, 250)
	length.grid(column = 0, row = 11)
	
	spacetxt = Label(tk, text = "Space: ", font = ("Arial", 20))
	spacetxt.grid(column = 0, row = 12)
	space = Spinbox(tk, from_=0, to=1000, width = 16)
	space.insert(END, 250)
	space.grid(column = 0, row = 13)
	
	shapetxt = Label(tk, text = "Shape: ", font = ("Arial", 20))
	shapetxt.grid(column = 0, row = 14)
	shape = Combobox(tk)
	shape["values"]= ("Classic", "Arrow", "Turtle", "Circle", "Square", "Triangle", "No Shape")
	shape.current(6)
	shape.grid(column = 0, row = 15)

	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 16, pady = 10)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 17, pady = 10)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 18)

	tk.mainloop()

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
