from tkinter import *

root = Tk()

# gemotery tells about size
root.geometry("720x720")
# minimum size:
root.minsize(400,768)
root.title("PC Assi")
# welcome = Label(text="Welcome to my GUI")
# welcome.pack()
# image = PhotoImage(file="background.png")
# image_label = Label(image=image)
# image_label.pack()
text_label = Label(text='''Hello this is the amamzing title of the while world
Hello this is the amamzing title of the while world
Hello this is the amamzing title of the while world
Hello this is the amamzing title of the while world''',
bg="red",fg="blue",padx="20",pady="20",font="timesnewroman 12 bold",borderwidth=3,relief=SUNKEN)
# pack attributes
# anchor
# side
# paddx,paddy,fill
# text_label.pack(side=BOTTOM,anchor = "se",fill="both")
text_label.pack(side=RIGHT,anchor = "se",padx=90,pady=90,fill=Y)
#  main gui loop
root.mainloop()