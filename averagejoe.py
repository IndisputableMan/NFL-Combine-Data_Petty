#from datetime import time
 # def load_data(playercombinedata.csv):
 #   mylist = []
 #   with open(playercombinedata.csv) as nflcombine:
 #       nflcombine_data = csv.reader(playercombinedata.csv, delimiter=',')
 #       for row in nflcombine_data:

import csv


u_mile = int(input("What is your current fastest mile, rounded up, in minutes?"))
#convert mile into 40 yard dash time
# need to divide miles into yards
u_fr = str(u_mile * .04)
print ('Your yards per minute is: ' + u_fr)



# 11-18-22: Need to learn how to return row about player from input 



