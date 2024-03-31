# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

# Loop
def loop():
	screen = turtle.Turtle()
	turtle.title("Circler Screen Saver")
	turtle.bgcolor("black")
	loop = 0
	circle = 0
	line = 0
	draw = 1
	exponent = int(exp.get()) + 1
	screen.color(color.get())
	screen.penup()
	screen.goto(0, -250)
	screen.pendown()
	# Shape selection
	if shape.get() == "No Shape":
		screen.hideturtle()
	else:
		screen.shape(shape.get().lower())
	screen.speed(int(speed.get()))
	while True:
		loop += 1
		print("Loop", loop)
		for x in range(0, int(time.get())): # Draw Circles
			screen.circle(draw)
			circle += 1
			draw *= int(exp.get())
			print("Circle", circle)
			print("Circle Size", draw)
		draw = 1
		# When using screen.reset, we have to redefine our screen properties
		screen.reset()
		screen.penup()
		screen.goto(0, -250)
		screen.pendown()
		screen.color(color.get())

# Initialize Tkinter Window
def screensaver():
	global color, exp, time, shape, speed
	def close():
		tk.destroy()
		turtle.bye()
		print("Closed Window")
	tk = Tk()
	tk.title("Circler Screen Saver Interface")
	title = Label(tk, text = "Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)
	
	colortxt = Label(tk, text = "Color: ", font = ("Arial", 20))
	colortxt.grid(column = 0, row = 2)
	color = Entry(tk, width = 16)
	color.insert(END, "white")
	color.grid(column = 0, row = 3)
	
	exptxt = Label(tk, text = "Exponent: ", font = ("Arial", 20))
	exptxt.grid(column = 0, row = 1)
	exp = Spinbox(tk, from_=2, to=100, width = 16)
	exp.grid(column = 0, row = 2)

	timetxt = Label(tk, text = "Times to Repeat the Circle: ", font = ("Arial", 20))
	timetxt.grid(column = 0, row = 3)
	time = Spinbox(tk, from_=0, to=100, width = 16)
	time.insert(END, 8)
	time.grid(column = 0, row = 4)

	shapetxt = Label(tk, text = "Shape: ", font = ("Arial", 20))
	shapetxt.grid(column = 0, row = 5)
	shape = Combobox(tk)
	shape["values"]= ("Classic", "Arrow", "Turtle", "Circle", "Square", "Triangle", "No Shape")
	shape.current(0)
	shape.grid(column = 0, row = 6)
	
	speedtxt = Label(tk, text = "Speed: ", font = ("Arial", 20))
	speedtxt.grid(column = 0, row = 7)
	speed = Spinbox(tk, from_=2, to=100, width = 16)
	speed.grid(column = 0, row = 8)
	
	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 9, pady = 10)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 10, pady = 10)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 11)

	tk.mainloop()

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
