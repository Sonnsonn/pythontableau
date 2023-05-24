# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:11:39 2022

@author: SONIA
"""

import pandas as pd

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv",sep=";")

CostPerItem = 11.73
SellingPricePerItem =21.11
NumberOfItemsPurchased =6

#mathematical operations on tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#cost per item entire column calculation
#format column calc is; variable =dataframe[column name] 

CostPerItem = data["CostPerItem"]
NumberOfItemsPurchased = data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#aadding a new column to dataframe
data["CostPerTransaction"] = CostPerTransaction
data["SellingPricePerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#profit = sales - cost
data["ProfitPerTransaction"] = data["SellingPricePerTransaction"] - data["CostPerTransaction"]

#markup = sales - cost/cost
data["Markup"] = data["ProfitPerTransaction"] / data["CostPerTransaction"]

#round up markup - ROUND(variable,digits)
roundmarkup = round(data["Markup"],2)

#combining the dates... first off you should xhange the variable from dtring to variable
Day = data['Day'].astype(str)
Year = data['Year'].astype(str)
Date = Day + '-' + data['Month'] + '-' + Year
data['Date'] = Date

#how to show only specific rows in a dataframe eg showing index 0
data.iloc[0]
#first 3 rows
data.iloc[0:3]
#last 5 rows
data.iloc[-5]
#you can also use data.head to bring in first 5 rows

#how to bring up specific rows and collumns; first row then column separated by comma
data.iloc[0,5]

#using split to separate variables in the same column
#format = column.str.split('sep', expand = True)

splitcol= data['ClientKeywords'].str.split(',' , expand = True)

#creating new colums for the split columns
data['ClientAge']= splitcol[0]
data['ClientType']= splitcol[1]
data['lengthOfContract']= splitcol[2]

#using the replace function to replace the brackets (in this instance with nothing)
data['ClientAge']= data['ClientAge'].str.replace('[','')
data['lengthOfContract'] =data['lengthOfContract'].str.replace(']','')

#changing words to lower case using the lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#olpening a new file into the existing program
#also using the separation function to seoarate the columns which seemed to merge upon opening
data2 = pd.read_csv('value_inc_seasons.csv')
data2 = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging the two files together
data= pd.merge(data, data2, on='Month')

#how to delete columns
data= data.drop('ClientKeywords', axis=1)
data= data.drop('Day', axis=1)
data= data.drop('Year', axis=1)
data= data.drop('Month', axis=1)

#export to a csv to become a file 
data.to_csv('ValueIncCleaned.csv', index= False)
#index= False means we want to exclude the index column because its useless as there is already an id number







