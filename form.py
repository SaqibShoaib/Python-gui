from tkinter import *
root = Tk()
root.geometry("720x720")
root.title("Text To Speach")
# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[0].id)
# engine.setProperty('voice',voices[0].id)
# newVoiceRate = 145
# engine.setProperty('rate',newVoiceRate)


# def speak():
#     audio = sender_output.get()
#     engine.say(audio)
    # engine.runAndWait()
# def submitdata():
#     print(f"The value of username is {uservalue.get()}")
#     print(f"The value of password is {passvalue.get()}")
# username = Label(root,text="Enter Username: ")
# password = Label(root,text="Enter Password: ")
# username.grid()
# password.grid(row=1)

# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root,textvariable = uservalue)
# passentry = Entry(root,textvariable = passvalue)
# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)

# b = Button(root,text="SUBMIT",command=submitdata)
# b.grid(rows=3,column=0)

# speaker_label = Label(root,text="Enter what you want to convert from text to speach: ",
# font="timesnewroman 14")
# speaker_label.grid(row=0)
# sender_output = StringVar()
# sender_output_display = Entry(root,textvariable = sender_output)
# sender_output_display.grid(row=2)
# submit = Button(root,text="Convert",command=speak)
# submit.grid(row=3)

def getvalues():
    with open("data.txt","a") as f:
        f.write(f"{name.get()}\t\t")
        f.write(f"{password.get()}\t\t\t")
        f.write(f"{gender.get()}\t\t")
        f.write(f"{phone.get()}\t\t")
        f.write(f"{pay_confirm}\n")
        Label(root,text="Data Submitted",font="timesnewroman 13").grid(row=8,column=2)
# heading
Label(root,text="Welocme to the form",padx=10,pady=10,font="timesnewroman 20 bold").grid(row=0,column=2)
Label(root,text="Enter Name Here: ").grid(row=1,column=0,padx=2)
Label(root,text="Enter Passsword Here: ").grid(row=2,column=0,padx=2)
Label(root,text="Enter Gender Here: ").grid(row=3,column=0,padx=2)
Label(root,text="Enter Phone Nubmer Here: ").grid(row=4,column=0,padx=2)
# variables
name = StringVar()
password = StringVar()
gender = StringVar()
phone = StringVar()
payment_methods = ["paypal","wire transfer","payoneer"]
pay_checkbox = IntVar()
pay_confirm = payment_methods[pay_checkbox.get()]
# entry point
Entry(root,textvariable=name).grid(row=1,column=2,pady=5)
Entry(root,textvariable=password).grid(row=2,column=2,pady=5)
Entry(root,textvariable=gender).grid(row=3,column=2,pady=5)
Entry(root,textvariable=phone).grid(row=4,column=2,pady=5)
# payment method heading
Label(root,text="Choose payment method below",font="timesnewroman 12").grid(row=5,column=2,pady=30)
Radiobutton(root,text="Paypal",variable=pay_checkbox,value=0).grid(row=6,column=0)
Radiobutton(root,text="Wire Transfer",variable=pay_checkbox,value=1).grid(row=6,column=2)
Radiobutton(root,text="Payooner",variable=pay_checkbox,value=2).grid(row=6,column=3)
Button(root,text="Submit",command=getvalues).grid(row=7,column=2,pady=20)


root.mainloop()