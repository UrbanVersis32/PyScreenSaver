# Infinite Turtles Screen Saver

# Imports
import turtle
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from time import *

def run(): # Loop for clock repetition
	print("Time: " + time)
	label.set()
	
# Loop
def loop():
	global time, label
	# Initialize Tkinter Clock Window
	screen = Tk()
	screen.title("Clock Screen Saver")
	screen.configure(background = backcolor.get())
	time = asctime()
	while True:
		# Create Label
		time = asctime()
		label = Label(screen, text = time, font = (font.get(), int(size.get())), foreground = color.get(), background = backcolor.get())
		label.grid(column = 0, row = 0)
		# We use the following code instead of tk.mainloop() to disable the code-stopping properties of tk.mainloop()
		screen.update_idletasks()
		screen.update()
		sleep(1)
	
# Initialize Tkinter Window
def screensaver():
	global backcolor, color, size, font
	def close():
		tk.destroy()
		screen.destroy()
		print("Closed Window")
	tk = Tk()
	tk.title("Clock Screen Saver Interface")
	title = Label(tk, text = "Screen Saver", font = ("Verdana", 40))
	title.grid(column = 0, row = 0)
	
	backcolortxt = Label(tk, text = "Background Color: ", font = ("Arial", 20))
	backcolortxt.grid(column = 0, row = 1)
	backcolor = Entry(tk, width = 16)
	backcolor.insert(END, "black")
	backcolor.grid(column = 0, row = 2)
	
	colortxt = Label(tk, text = "Color: ", font = ("Arial", 20))
	colortxt.grid(column = 0, row = 3)
	color = Entry(tk, width = 16)
	color.insert(END, "green")
	color.grid(column = 0, row = 4)
	
	sizetxt = Label(tk, text = "Font Size: ", font = ("Arial", 20))
	sizetxt.grid(column = 0, row = 5)
	size = Spinbox(tk, from_=0, to=100, width = 16)
	size.insert(END, 36)
	size.grid(column = 0, row = 6)

	fonttxt = Label(tk, text = "Font: ", font = ("Arial", 20))
	fonttxt.grid(column = 0, row = 7)
	font = Entry(tk, width = 16)
	font.insert(END, "Courier New")
	font.grid(column = 0, row = 8)
	
	load = Button(tk, text = "Load Screen Saver", command = loop)
	load.grid(column = 0, row = 9, pady = 11)

	close = Button(tk, text = "Close", command = close)
	close.grid(column = 0, row = 10, pady = 12)

	info = Label(tk, text = "By Urban Versis 32", font = ("Arial", 10))
	info.grid(column = 0, row = 11)
	
	tk.mainloop

# Run and Developer Stuff
if __name__ == "__main__":
    screensaver()
