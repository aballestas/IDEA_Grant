# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:10:46 2020

@author: antob
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:57:03 2020

@author: antob
"""

import pandas as pd 
import matplotlib.pyplot as plt


#loads the Google Movement data
movement_df = pd.read_csv("Global_Mobility_Report(4).csv")

GroceryMovement_filtered = movement_df.loc[movement_df["sub_region_1"] ==  "Florida",["date","grocery", "sub_region_2"]]

GroceryMovement_df = pd.DataFrame(GroceryMovement_filtered)




#deletes the empty counties 
GroceryMovement_df.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


#fills in empty grocery values
GroceryMovement_df.fillna(value = 0 )




#this strips the data a KEY and it's date and delta_change it's VALUE
dates_per_county = {}

for index,row in GroceryMovement_df.iterrows():
    date = row["date"]
    county_date_change = (row["grocery"])
    if date in dates_per_county:
        dates_per_county[date].append(county_date_change)
    else: 
        dates_per_county[date] = [county_date_change]
#print (dates_per_county)


print("This is the length of the values list, should also be the number of counties")
print (len(dates_per_county['2/15/20']))   


#This is the number of counties
first_dates = dates_per_county[next(iter(dates_per_county))]
number_of_Counties = len(first_dates)

print ("Checking if this number matches above: " + str(number_of_Counties))

#This ensures that all dates have the same number of obs which is the number of counties 
for date in dates_per_county.keys(): 
    length_of_values = len(dates_per_county[date]) 
    if length_of_values < number_of_Counties:
        missing_ammount = number_of_Counties - length_of_values
        for i in range(missing_ammount):
            dates_per_county[date].append(0)


num_big_deltas_per_date = {}

print("this is the lenth of dates per county keys:")
print(len(dates_per_county.keys()))



for key in dates_per_county.keys():
    num_big_deltas_per_date[key] = 0
#print (num_big_deltas_per_date)

#This tally's the number of counties that are 'infected' or panic buying 
#aka over 5% movement     
for i in range(number_of_Counties):
    for date in dates_per_county.keys():
        delta = dates_per_county[date][i]
        if i < 20: 
            if delta >= 5.0:
                num_big_deltas_per_date[date] += 1
        else: 
            if delta >= -3.0:  
                num_big_deltas_per_date[date] += 1

print("This is the num_big_deltas output")
print(len(num_big_deltas_per_date))
print(num_big_deltas_per_date)

delta_df = df = pd.DataFrame.from_dict(num_big_deltas_per_date, orient="index")
delta_df.to_csv (path_or_buf ='TEST_Florida_grocery_movement.csv',index = True)
delta_df.plot()
plt.show()