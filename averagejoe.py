#from datetime import time
 # def load_data(playercombinedata.csv):
 #   mylist = []
 #   with open(playercombinedata.csv) as nflcombine:
 #       nflcombine_data = csv.reader(playercombinedata.csv, delimiter=',')
 #       for row in nflcombine_data:

# u_mile = int(input("What is your current fastest mile, rounded up, in minutes?"))
# convert mile into 40 yard dash time
# need to divide miles into yards
# u_fr = str(u_mile * .04)
#print ('Your yards per minute is: ' + u_fr)
# 11-18-22: Need to learn how to return row about player from input 

import csv
import pandas as pd


#Dimensions of football field in yards
fld_len = 100
fld_wdth = 53.33

# dataframe from combine data
nfl = pd.read_csv("playercombinedata.csv") 

# Use this statement to  print out by postion from the nfl dataframe: print (nfl.groupby('POS').get_group('CB'))

# Dataframe that is the 10 year span from 2008-2018
draft = nfl[nfl['Year']>= 2008]

# Lists for offense and defense 
offense = ['FB','G','K','LS','OG','OL','OT','P','QB','RB','TE','WR']
defense = ['CB', 'DB','DE','DL','DT','FS','ILB','LB','NT','OLB', 'SS']

# Created new defense dataframe based on defense list,using isin method.  
def_df = draft[draft['POS'].isin(defense)]

# Prints out the average 40 Yard Dash per defensive position from 2008 - 2018, using the def_df dataframe 
pos_speed = def_df.groupby('POS')['40 Yard'].mean()
print(pos_speed)

# This statement counts number of positons used to make the average 40 yard dash speed for draft dataframe: print (draft.groupby('POS')['40 Yard'].count()) 

print ('\n' + 'DONE')

strong_sde = 59.3/2
print ( (pos_speed[0])/8)

# NEXT GOAL: Retreive data from the last 4 years in the NFL Combine
