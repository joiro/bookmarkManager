from Tkinter import *
import requests
from json import *
from urllib2 import *
import io
import csv

url = "http://data.nottinghamtravelwise.org.uk/parking.csv?noLocation=true?t=635509084580321642"
webpage = urlopen(url)

datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = list(datareader)


substring = data[0][-1]
# Capacity, Name, Occupancy, Occ.Percentage for each Location 
'''
for i in range(1,len(data)):
    cap = data[i][1]
    name = data[i][3]
    occ = data[i][-6]
    occp = data[i][-5]
    dataone = data[i][-1]
    print name
    print occp +"%"
    print occ + " of" + cap + " filled"
    print "Last updated: " + dataone
'''
# Number of total locations
def number_of_spaces():
    x = len(data)-1
    print x

# Complete Part
'''
# Total Capacity
# Total Space filled
# Total Percentage filled
capall = 0
occall = 0
occpall = 0
for i in range(1,len(data)):
    capall = capall + int(data[i][1])
    occall = occall + int(data[i][-6])
    occpall = occpall + int(data[i][-5])
    
percall = occpall/(len(data)-1)
print "Percentage filled: " + str(percall) +"%"
print "Total available: " + str(capall)
print "Spaces filled: " + str(occall)
'''
capall = 1
occall = -6
occpall = -5
def calc_x(y):    
    x = 0
    for i in range(1,len(data)):
        x = x + int(data[i][y])
    print x
calc_x(occpall)
