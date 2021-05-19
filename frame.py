from tkinter import *
root = Tk()

root.geometry("720x720")
root.title("frame")
f = Frame(root,borderwidth=5,bg="grey",relief=SUNKEN)
f.pack(side=TOP,fill="x")
f2 = Frame(root,borderwidth=20,bg="red",relief=SUNKEN)
f2.pack(side=TOP,fill="y")
l = Label(f,text='''This is the world's best line''',
bg="white",font="timesnewroman 20 bold",
fg="yellow")
l.pack(side=LEFT,fill="y",pady=20,padx=20)
l2 = Label(f2,text="This is the world's second best title on left side",
bg="pink",font="sansserif 20 bold")
l2.pack()
root.mainloop()