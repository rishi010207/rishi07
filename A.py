#Module Importing
from tkinter import *

root = Tk()                  #Window creation
canvas_width = 500           #Canvas width definition
canvas_height = 500          #Canvas height definition

#Canvas creation and display
canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = "green")
canvas.pack()

#Line creation
y = int(canvas_height/2)
canvas.create_line(10, y, canvas_width, y, fill = "blue")

#Arc creation
coordinates = 10,50,240,210
arc = canvas.create_arc(coordinates, start = 90, extent = 190, fill = "red")

#Oval creation
oval = canvas.create_oval(50, 60, 100, 100)

#Program Loop
root.mainloop()
