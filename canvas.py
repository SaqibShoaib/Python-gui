from tkinter import *

root = Tk()
Canvas_width = 400
Canvas_height = 600
root.geometry(f"{Canvas_width}x{Canvas_height}")
root.title("Canvas")
can_wid = Canvas(root,width=Canvas_width,height=Canvas_height)
can_wid.pack()
# can_wid.create_line(0,0,200,300)
# # can_wid.create_line(400,0,200,300)
# can_wid.create_line(0,300,200,300)
# can_wid.create_line(200,0,200,300)

# to create rectangle enter top left cornor point and bottom right corner
can_wid.create_rectangle(10,10,390,590,fill="pink")
# create text will take only position of point
# can_wid.create_text(200,300,text="GUI=Graphical \nUser Interface",fill="green",font="timesnewroman 20 bold")
# create ovel will take the same parameters like rectangle
can_wid.create_oval(100,100,300,300,fill="white")
root.mainloop()