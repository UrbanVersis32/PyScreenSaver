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
	turtle.title("Hexagonal Screen Saver")
	colors = [color1.get(), color2.get(), color3.get(), color4.get(), color5.get(), color6.get()] # Colors list
	turtle.bgcolor("black")
	print("Selected Colors: " + str(colors))
	loop = 0
	hex = 0
	circle = 0
	line = 0
	while True:
		# Shape selection
		if shape.get() == "No Shape":
			screen.hideturtle()
		else:
			completeshape = shape.get().lower()
			
		screen.shape(completeshape)
		screen.speed(int(speed.get()))
		loop += 1
		print("Loop", loop)
		for n in range(int(time.get())): # Draw Hexagons
			hex += 1
			print("Hexagon", hex)
			for i in range(6):
				line += 1
				print("Line", line)
				screen.color(colors[i])
				screen.forward(int(size.get()))
				screen.left(int(length.get()))
			screen.right(int(space.get()))
		screen.penup()
		screen.color('white')
		
		for i in range(36): # Draw circles
			circle += 1
			print("Circle", circle)
			screen.forward(220)
			screen.color(color1.get())
			screen.pendown()
			screen.begin_fill()
			screen.circle(7)
			screen.end_fill()
			screen.penup()
			screen.backward(220)
			screen.right(10)
		screen.reset()

# Initialize Tkinter Window
def screensaver():
	global color1, color2, color3, color4, color5, color6, speed, size, length, space, time, shape
	def close():
		tk.destroy()
		turtle.bye()
		print("Closed Window")
	tk = Tk()
	tk.title("Hexagonal Screen Saver Interface")
	title = Label(tk, text = "Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)

	color1txt = Label(tk, text = "Color 1: ", font = ("Arial", 20))
	color1txt.grid(column = 0, row = 2)
	color1 = Entry(tk, width = 16)
	color1.insert(END, "red")
	color1.grid(column = 0, row = 3)

	color2txt = Label(tk, text = "Color 2: ", font = ("Arial", 20))
	color2txt.grid(column = 0, row = 4)
	color2 = Entry(tk, width = 16)
	color2.insert(END, "yellow")
	color2.grid(column = 0, row = 5)

	color3txt = Label(tk, text = "Color 3: ", font = ("Arial", 20))
	color3txt.grid(column = 0, row = 6)
	color3 = Entry(tk, width = 16)
	color3.insert(END, "blue")
	color3.grid(column = 0, row = 7)

	color4txt = Label(tk, text = "Color 4: ", font = ("Arial", 20))
	color4txt.grid(column = 0, row = 8)
	color4 = Entry(tk, width = 16)
	color4.insert(END, "darkorange")
	color4.grid(column = 0, row = 9)

	color5txt = Label(tk, text = "Color 5: ", font = ("Arial", 20))
	color5txt.grid(column = 0, row = 10)
	color5 = Entry(tk, width = 16)
	color5.insert(END, "lime")
	color5.grid(column = 0, row = 11)

	color6txt = Label(tk, text = "Color 6: ", font = ("Arial", 20))
	color6txt.grid(column = 0, row = 12)
	color6 = Entry(tk, width = 16)
	color6.insert(END, "red")
	color6.grid(column = 0, row = 13)

	speedtxt = Label(tk, text = "Speed: ", font = ("Arial", 20))
	speedtxt.grid(column = 0, row = 14)
	speed = Spinbox(tk, from_=2, to=100, width = 16)
	speed.grid(column = 0, row = 15)

	sizetxt = Label(tk, text = "Size: ", font = ("Arial", 20))
	sizetxt.grid(column = 0, row = 16)
	size = Spinbox(tk, from_=0, to=1000, width = 16)
	size.insert(END, 100)
	size.grid(column = 0, row = 17)

	lengthtxt = Label(tk, text = "Length: ", font = ("Arial", 20))
	lengthtxt.grid(column = 0, row = 18)
	length = Spinbox(tk, from_=0, to=500, width = 16)
	length.insert(END, 60)
	length.grid(column = 0, row = 19)

	spacetxt = Label(tk, text = "Space: ", font = ("Arial", 20))
	spacetxt.grid(column = 0, row = 20)
	space = Spinbox(tk, from_=0, to=100, width = 16)
	space.insert(END, 10)
	space.grid(column = 0, row = 21)

	timetxt = Label(tk, text = "Times to Repeat: ", font = ("Arial", 20))
	timetxt.grid(column = 0, row = 22)
	time = Spinbox(tk, from_=0, to=100, width = 16)
	time.insert(END, 36)
	time.grid(column = 0, row = 23)

	shapetxt = Label(tk, text = "Shape: ", font = ("Arial", 20))
	shapetxt.grid(column = 0, row = 24)
	shape = Combobox(tk)
	shape["values"]= ("Classic", "Arrow", "Turtle", "Circle", "Square", "Triangle", "No Shape")
	shape.current(0)
	shape.grid(column = 0, row = 25)

	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 26, pady = 10)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 27, pady = 10)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 28)

	tk.mainloop()

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
