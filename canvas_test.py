from Tkinter import *
from urllib2 import *
import csv

root = Tk()

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)

datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)



class can(Canvas):

    def __init__(self,tk):
        Canvas.__init__(self,tk)
        self.config(bd=1)
        self.config(relief="solid")

class Fram(Frame):

    def __init__(self,tk,width,height):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(relief="solid")


Canone = can(root)
Canone.config(width=500,height=60)
Canone.grid(row=0,column=0)

mainloop()
