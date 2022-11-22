import csv
import pandas as pd


#list both .csv files

nfl = pd.read_csv("playercombinedata.csv") 
nfl2022 = pd.read_csv("playercombinedata2022.csv") 
nfl2022.insert(0,'Year',2022,allow_duplicates= False)

nfl2022.rename(columns= {'WT':'Weight(lbs)', '40yd': '40 Yard', 'Vertical':'Vert Leap(in)',
                            'Broad Jump':'Broad Jump(in)', 'Bench':'Bench Pres',
                            'Player': 'Name', 'College': 'Secondary Type', 'Ht': 'Height (in)',
                            'School': 'College', 'Pos': 'POS', 
                             }, inplace = True)

nfl_df = pd.concat([nfl,nfl2022],axis = 1, join = 'outer')

# print (nfl_df)
#print(nfl_df.columns)

nfl_df.to_csv('nfl_combine_csv')




