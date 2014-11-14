from Tkinter import *
import requests
from json import *
from urllib import *
import urllib.request

class Fram(Frame):

    def __init__(self,tk,width,height):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bd=1)
        self.config(relief="solid")

class Lab(Label):

    def __init__(self,tk,text):
        Label.__init__(self,tk)
        self.config(text=text)
        self.config(font=("Helvetica","12"))
        
class NavButton(Button):

    def __init__(self,tk,text):
        Button.__init__(self,tk)
        self.config(text=text)


data = urllib.request.urlopen("http://data.nottinghamtravelwise.org.uk/parking.json?noLocation=true?t=635509084580321642")
text = data.read().decode("utf8")
print text

root = Tk()
root.title("Parking Lot Info")


# Frames
Ov = Lab(root,text="Overview")
Ov.config(bg="grey")
Ov.pack(fill="x",anchor="w")
header = Fram(root,509,60)
header.config(bg="grey",bd=0)
header.pack()
mainFrame = Fram(root,500,2000)
mainFrame.config(bd=0)
mainFrame.pack()

title = Fram(mainFrame,500,20)
title.config(bd=0)
title.grid(row=2,column=0)
TitLab = Lab(title,"Car Parks")
TitLab.pack()
conta = Fram(mainFrame,500,40).grid(row=3,column=0,padx=3,pady=3)
contb = Fram(mainFrame,500,40).grid(row=4,column=0,padx=3,pady=3)
contc = Fram(mainFrame,500,40).grid(row=5,column=0,padx=3,pady=3)
contd = Fram(mainFrame,500,40).grid(row=6,column=0,padx=3,pady=3)
conte = Fram(mainFrame,500,40).grid(row=7,column=0,padx=3,pady=3)
button = Fram(mainFrame,500,30)
button.config(bd=0)
button.grid(row=8,column=0)
footer = Fram(mainFrame,500,20)
footer.config(bd=0)
footer.grid(row=9,column=0)

# Botton NavButtons
ButtonLeft = NavButton(button,"<").pack(side=LEFT)
ButtonRight = NavButton(button,">").pack(side=LEFT)

# Label
Foot = Lab(footer,"Contains Public Sector Information licensed under the Open Government License v.1.0.").pack()

mainloop()
