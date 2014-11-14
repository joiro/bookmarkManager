from Tkinter import *
from urllib2 import *
import csv

class Fram(Frame):

    def __init__(self,tk,width,height):
        Frame.__init__(self,tk)
        self.config(width=width)
        self.config(height=height)
        self.config(bd=1)
        self.config(relief="solid")

    def calc_xx(self):
        print "Spaces filled: "

class can(Canvas):

    def __init__(self,tk):
        Canvas.__init__(self,tk)
        self.config(relief="solid")

class Lab(Label):

    def __init__(self,tk):
        Label.__init__(self,tk)
        self.config(font=("Helvetica","12"))

class NavButton(Button):

    def __init__(self,tk,text):
        Button.__init__(self,tk)
        self.config(text=text)

root = Tk()
root.title("Parking Lot Info")

# text = webpage.read().decode("utf8")

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)

datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)

# OVERVIEW

# Spaces Filled
# Spaces Available
# Percentage Filled


capacity_t = 1
occup_t = -6
occup_t_perc = -5
def calc_x(y):
    x = 0
    if y == occup_t_perc:
        for i in range(1,len(data)):
            x = x + int(data[i][y])
            t = x/(len(data)-1)
        print str(t)+"%"
    else:
        for i in range(1,len(data)):
            x = x + int(data[i][y])
        print x 

v = StringVar()
b = "{:<3} {:<22} {:<25} {:<1}".format("Spaces Filled: "+data[1][-6]+"Spaces Available: "+data[1][1]+"Percentage Filled: "+data[1][-5]+"%")
# "Statuses"

# Spaces (Calculates number of total locations)
def num_of_total_spaces():
    x = len(data)-1
    print x

# Full (Should show the number of locations where occupancy = 100%)

# Almost full (Should show the number of locations where occupancy = 80%)

# Faulty


# LOCATION DETAILS
# Capacity, Name, Occupancy, Occ.Percentage for each Location 
def specs_loc(m):
    print "Location: " + data[m][3]
    print data[m][-5] +"%"
    print data[m][-6] + " of" + data[m][1] + " filled"
    print "Last updated: " + data[m][-1]


# LAYOUT CONSTRUCTION SIDE


# Layout Frames for title, header
Ov = Lab(root)
Ov.config(bg="grey",text="Overview")
Ov.pack(fill="x",anchor="w")

header = Fram(root,509,60)
header.config(bg="grey",bd=0)
header.pack()
headlab = Lab(header)
headlab.config(bg="grey",textvariable=v)
headlab.grid(row=1,column=0)
v.set(b)

mainFrame = Fram(root,500,2000)
mainFrame.config(bd=0)
mainFrame.pack()

title = Fram(mainFrame,500,20)
title.config(bd=0)
title.grid(row=2,column=0)

TitLab = Lab(title)
TitLab.config(text="Car Parks")
TitLab.grid(row=3)

# Layout Frames for each parking location
conta = Fram(mainFrame,500,40).grid(row=4,column=0,padx=3,pady=3)
contb = Fram(mainFrame,500,40).grid(row=5,column=0,padx=3,pady=3)
contc = Fram(mainFrame,500,40).grid(row=6,column=0,padx=3,pady=3)
contd = Fram(mainFrame,500,40).grid(row=7,column=0,padx=3,pady=3)
conte = Fram(mainFrame,500,40).grid(row=8,column=0,padx=3,pady=3)

button = Fram(mainFrame,500,30)
button.config(bd=0)
button.grid(row=9,column=0)

footer = Fram(mainFrame,500,20)
footer.config(bd=0)
footer.grid(row=10,column=0)

# Botton Navigation buttons
ButtonLeft = NavButton(button,"<").pack(side=LEFT)
ButtonRight = NavButton(button,">").pack(side=LEFT)

# Label at the bottom, displaying license information
Foot = Lab(footer)
Foot.config(text="Contains Public Sector Information licensed under the Open Government License v.1.0.")
Foot.pack()

mainloop()
