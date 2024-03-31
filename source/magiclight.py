# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from time import *

# Loop
def loop():
	screen = turtle.Turtle()
	turtle.title("Magic Light Screen Saver")
	turtle.bgcolor("black")
	loop = 0
	line = 0
	screen.color(color.get())
	# Draw the circle in the center
	point = turtle.Turtle()
	point.color(color.get())
	point.shape("circle")
	
	screen.speed(int(speed.get()))
	while True:
		# Shape selection
		if shape.get() == "No Shape":
			screen.hideturtle()
		else:
			screen.shape(shape.get().lower())
		loop += 1
		print("Loop", loop)
		for x in range(0, 10): # Draw The Magic Light
			line += 1
			print("Line", line)
			if direction.get() == "Clockwise":
				screen.left(36)
			elif direction.get() == "Counter Clockwise":
				screen.right(36)
			screen.forward(int(length.get()))
			screen.backward(int(length.get()))
			sleep(1)
		# When using screen.reset, we have to redefine our screen properties
		screen.reset()
		screen.color(color.get())
	
# Initialize Tkinter Window
def screensaver():
	global color, length, shape, speed, direction
	def close():
		tk.destroy()
		turtle.bye()
		print("Closed Window")
	tk = Tk()
	tk.title("Magic Light Screen Saver Interface")
	title = Label(tk, text = "Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)
	
	colortxt = Label(tk, text = "Color: ", font = ("Arial", 20))
	colortxt.grid(column = 0, row = 1)
	color = Entry(tk, width = 16)
	color.insert(END, "white")
	color.grid(column = 0, row = 2)
	
	lengthtxt = Label(tk, text = "Length: ", font = ("Arial", 20))
	lengthtxt.grid(column = 0, row = 3)
	length = Spinbox(tk, from_=0, to=100, width = 16)
	length.insert(END, 100)
	length.grid(column = 0, row = 4)

	shapetxt = Label(tk, text = "Shape: ", font = ("Arial", 20))
	shapetxt.grid(column = 0, row = 5)
	shape = Combobox(tk)
	shape["values"]= ("Classic", "Arrow", "Turtle", "Circle", "Square", "Triangle", "No Shape")
	shape.current(6)
	shape.grid(column = 0, row = 6)
	
	speedtxt = Label(tk, text = "Speed: ", font = ("Arial", 20))
	speedtxt.grid(column = 0, row = 7)
	speed = Spinbox(tk, from_=0, to=100, width = 16)
	speed.insert(END, 5)
	speed.grid(column = 0, row = 8)
	
	directiontxt = Label(tk, text = "Direction: ", font = ("Arial", 20))
	directiontxt.grid(column = 0, row = 9)
	direction = Combobox(tk)
	direction["values"]= ("Counter Clockwise", "Clockwise")
	direction.current(0)
	direction.grid(column = 0, row = 10)
	
	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 11, pady = 11)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 12, pady = 12)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 13)

	tk.mainloop()

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
