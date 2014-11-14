from Tkinter import *
from urllib2 import *
import csv

root = Tk()
root.title("Parking Lot Info")

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)

datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)

a = StringVar()
b = "Last updated: " + data[1][-1]

class Fram(Frame):

    def __init__(self,tk,width,height):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bd=1)
        self.config(relief="solid")

class Lab(Label):

    def __init__(self,tk,width,height,textvariable):
        Label.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(textvariable=textvariable)
        self.config(font=("Helvetica","12"))

conta = Fram(root,70,5).grid(row=3,column=0,padx=3,pady=3)

Labelo = Lab(conta,60,5,textvariable=a)
Labelo.config(bg="grey")
Labelo.grid(row=3,column=0)
a.set(b)

mainloop()
