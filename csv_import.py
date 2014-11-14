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
def specs_loc(m):
    print "Location: " + data[m][3]
    print data[m][-5] +"%"
    print data[m][-6] + " of" + data[m][1] + " filled"
    print "Last updated: " + data[m][-1]


'''
# Number of total locations
def num_of_total_spaces():
    x = len(data)-1
    print x
'''
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

'''
capacity_t = 0
occup_t = 0
occup_t_perc = 0
for i in range(1,len(data)):
    capacity_t = capacity_t + int(data[i][1])
    occup_t = occup_t + int(data[i][-6])
    occup_t_perc = occup_t_perc + int(data[i][-5])
    
t = occup_t_perc/(len(data)-1)
print "Total available: " + str(capacity_t)
print "Spaces filled: " + str(occup_t)
print "Percentage filled: " + str(t) +"%"
'''
