from tkinter import *

root = Tk()

#!take input
line1= float(input("Whats the length of your first line? :"))
line2=float(input("whats the length of your second line? :"))
root.geometry('300x300')

canvas = Canvas(root, width=300, height=300)
canvas.pack()

#!create geometry here (not realated to root.geometry)
#vars
xstart_point = 10
ystart_point = 10

xline1_endpoint = xstart_point
yline1_endpoint = ystart_point + line1

xline2_endpoint = xstart_point + line2
yline2_endpoint = ystart_point + line1 
#code
entry= Entry(root, width = 40)
entry.focus_set()
entry.pack
canvas.create_line(xstart_point, ystart_point, xline1_endpoint, yline1_endpoint)
canvas.create_line(xline1_endpoint, yline1_endpoint, xline2_endpoint, yline2_endpoint)
canvas.create_line(xline2_endpoint, yline2_endpoint, xstart_point, ystart_point)

root.mainloop()