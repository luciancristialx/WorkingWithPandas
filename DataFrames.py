import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]

#Define dataframe
df = pd.DataFrame(data = [A,B,C,D,E],index = ['a','b','c','d','e'], columns = ['W', 'X', 'Y', 'Z'])
print("DataFrame:\n\n", df,"\n--------------------------------\n")
print("Print element from first column and first row: ",df.loc['a','W'],"\n--------------------------------\n")
print("Print first row:\n", df.loc['a'],"\n--------------------------------\n")
print("Print first row (numeric indexes):\n", df.iloc[0],"\n--------------------------------\n")

#Conditional selection
# print("Conditional selection:\n",df > 3,"\n--------------------------------\n")

#Conditional selection where values are greater than 3
# print("Conditional selection (where values are greater than 3):\n",df[df > 3],"\n--------------------------------\n")

#Conditional selection where values within a certain column are greater than 1
# print("Conditional selection (where values within a certain column are greater than 1):\n",df[df['Y'] > 1],
#     "\n--------------------------------\n")

#Conditional selection where values within a certain column are greater than 1 and print only column X, Z
# print("Conditional selection (where values within a certain column are greater than 1):\n",df[df['Y'] > 1][['X','Z']],
#     "\n--------------------------------\n")

#Conditional selection - multiple conditions
print("Conditional selection - multiple conditions:\n",df[(df['W']>3) & (df['Z']>2)],
    "\n--------------------------------\n")

# print("Print elements in first column:")
# for rowIndex in df.index:
#     print(df['W'][rowIndex])
# print("--------------------------------")

# Add column
# df['P'] = df['Y']+df['Z']
# print("DataFrame + new column:\n\n", df,"\n--------------------------------\n")

#Remove row (axis 0) - temporary (inplace False) / permanently
# df.drop('e', inplace = False)
# print("DataFrame - row e removed:\n\n", df,"\n--------------------------------\n")

#Remove column (axis 1) - temporary (inplace False) / permanently
# df.drop('P', axis = 1 , inplace = False )
# print("DataFrame - column P removed:\n\n", df,"\n--------------------------------\n")

# print("Read data from CSV and format output as following:\n")
# ReportData = pd.read_csv("TestingFile.csv")
# # print(ReportData)
#
# for i in range(len(ReportData)):
#     print(ReportData.iloc[i,0],'->',ReportData.iloc[i,0],'->',ReportData.iloc[i,3])
# print("--------------------------------")