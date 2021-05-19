from tkinter import *
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)


def speak():
    audio ="Hello Saqib"
    engine.say(audio)
    engine.runAndWait()
root = Tk()
root.geometry('720x720')
root.title("Button")
navbar = Frame(root)
navbar.pack(side=TOP,anchor="nw")
def hello():
    print("Hello world")
b = Button(navbar,padx=5,pady=5,text="Home",borderwidth=2,font="timesnewroman 10",command=hello)
b.pack(side=LEFT,padx=2) 
b2 = Button(navbar,padx=5,pady=5,text="Home",borderwidth=2,font="timesnewroman 10",command=hello)
b2.pack(side=LEFT,padx=2) 
b3 = Button(navbar,padx=5,pady=5,text="Home",borderwidth=2,font="timesnewroman 10",command=hello)
b3.pack(side=LEFT,padx=2) 
b4 = Button(navbar,padx=5,pady=5,text="Home",borderwidth=2,font="timesnewroman 10",command=hello)
b4.pack(side=LEFT,padx=2) 
b5 = Button(navbar,padx=5,pady=5,text="Call my name",borderwidth=2,font="timesnewroman 10",command=speak)
b5.pack(side=LEFT,padx=2) 
root.mainloop()