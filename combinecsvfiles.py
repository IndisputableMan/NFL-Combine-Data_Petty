import csv
import pandas as pd


#list both .csv files

nfl = pd.read_csv("playercombinedata.csv") 
nfl2022 = pd.read_csv("playercombinedata2022.csv") 
nfl2022.insert(0,'Year',2022,allow_duplicates= False)

nfl2022.rename(columns= {'Player':'Name', 'School':'College', 'College': 'Secondary Type', 'Ht':'Height'})

print (nfl2022.columns)
print (nfl.columns)





