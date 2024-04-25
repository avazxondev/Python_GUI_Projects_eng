import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root=Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#8EE5EE")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', 'english_rp+m3')
            engine.say(text)
            engine.runAndWait()

        else:
            engine.setProperty('voice', 'english_rp+f3')
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()





def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

        

#icon if you use windows os these two codeline working/ don't need to Linux os 
# image_icon = tk.PhotoImage(file='speak.png')
# root.iconphoto(False, image_icon)

#Top Frame

Top_Frame = Frame(root, bg='#7AC5CD', width=900, height=110)
Top_Frame.place(x=0, y=0)

Logo = PhotoImage(file='mic3.png')
Label(Top_Frame,image=Logo,bg='#7AC5CD').place(x=10,y=5)
Label(Top_Frame,text="TEXT TO SPEECH", font='arila 20 bold',bg='#7AC5CD',fg='black').place(x=120, y=30)

####### Text area 

text_area = Text(root,font='Robote 20',bg='white',relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150,width=500, height=250)

Label(root, text="VOICE",font='arial 15 bold',bg="#8EE5EE",fg='black').place(x=580,y=160)
Label(root, text="SPEED",font='arial 15 bold',bg="#8EE5EE",fg='black').place(x=750,y=160)

## gender combobox

gender_combobox=Combobox(root,values=['Male', 'Female'],font='Arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast', "Normal", 'Slow'],font='Arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set("Normal")

imagineicon1 = tk.PhotoImage(file='speak.png')
btn1 = Button(root,text='Speak',compound=RIGHT,image=imagineicon1, width=130,font='arial 14 bold',command=speaknow)
btn1.place(x=550, y=280)

imagineicon2 = tk.PhotoImage(file='save.png')
btn2 = Button(root,text='Save',compound=RIGHT,image=imagineicon2,bg='#39c790', width=130,font='arial 14 bold',command=download)
btn2.place(x=730, y=280)

root.mainloop()
