from tkinter import *
import tkinter.messagebox as tmsg
def getval():
    tmsg.showinfo("Money Added",f"The Money {myslider.get()} has been added to Your account")
root = Tk()
root.geometry("720x720")
root.title("Slider")
Label(text="Get Free Dollars",font="timesnewroman 12 bold").pack()
myslider = Scale(root,from_=0, to=200, orient=HORIZONTAL,tickinterval=100,length=200)
myslider.pack()
lb = Listbox(root)
lb.insert(END,10)
lb.pack()
# print(lb.get())
Button(text="Get Dollars",command=getval).pack()
root.mainloop()