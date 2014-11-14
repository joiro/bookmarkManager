from Tkinter import *
from urllib2 import *
import csv

root = Tk()

class Fram(Frame):

    def __init__(self,tk,width,height):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bd=1)
        self.config(relief="solid")
        self.url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
        self.webpage = urlopen(self.url)
        self.datareader = csv.reader(self.webpage.read().decode('utf-8').splitlines())
        self.data = list(self.datareader)
        self.a = 1
        self.b = -6
        self.c = -5
        self.value = self.calc_x(self.a, self.data)
        self.label = Label(self, text=self.value)
        self.label.pack()

    def calc_x(self, y, data):
        x = 0
        if y == self.c:
            for i in range(1,len(data)):
                x = x + int(data[i][y])
                t = x/(len(data)-1)
            return str(t)+'%'
        else:
            for i in range(1,len(data)):
                x = x + int(data[i][y])
            return str(x)

square_frame = Fram(root,500,40).grid(row=0,column=0,padx=3,pady=3)

mainloop()
