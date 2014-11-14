from Tkinter import *
import requests
from json import *
from urllib import *


class MainCanvas(Canvas):

    def __init__(self,tk,width,height,bg):
        Canvas.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bg=bg)

class NavButton(Button):

    def __init__(self,tk,text):
        Button.__init__(self,tk)
        self.config(text=text)

class Fram(Frame):

    def __init__(self,tk,width,height,bg):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bg=bg)

        
root = Tk()
root.title("Parking Lot Info")

greyField = MainCanvas(root,500,100,"grey")
greyField.create_text(10,10,anchor="nw",text="Overview")
greyField.pack()
can = MainCanvas(root,500,300,"white")
can.pack()

buttonFrame = Fram(root,70,5,"blue")
buttonFrame.config(bd=
buttonFrame.pack()

leftButton = NavButton(buttonFrame,"<")
leftButton.pack(side=BOTTOM,anchor=W)
rightButton = NavButton(buttonFrame,">")
rightButton.pack(side=BOTTOM,anchor=E)



mainloop()
