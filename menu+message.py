from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("720x800")
root.title("Menu")

def help_btn():
    tmsg.showinfo("Help","I will help You")
def myfun():
    print("Hello world")
def rate_btn():
    a = tmsg.askquestion("Rate us","You Used our GUI How was Your Experience?\
        \nDo you like it or not")
    print(a)
def chuss_btn():
    a = tmsg.askretrycancel("Chuss","Are You Single?")
    if a:
        tmsg.showinfo("TA TA","Tera kuch ni hoskta.")
    else:
        tmsg.showinfo("Hurrah","aap be life mai pet he rhe hoge")
mainmenu = Menu(root)
m = Menu(mainmenu,tearoff=0)
m.add_command(label="New Project",command=myfun)
m.add_command(label="Open file",command=myfun)
m.add_command(label="New Window",command=myfun)
m.add_command(label="Open Project",command=myfun)
m.add_command(label="add to folder",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m)
m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="About Us",command=help_btn)
m2.add_command(label="Rate Us",command=rate_btn)
m2.add_command(label="Chuss",command=chuss_btn)
mainmenu.add_cascade(label="Help",menu=m2)

root.mainloop()