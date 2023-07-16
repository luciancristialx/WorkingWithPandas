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
print("Print element from first column and first row: ",df['W'][0],"\n--------------------------------\n")

print("Print elements in first column:")
for rowIndex in df.index:
    print(df['W'][rowIndex])
print("--------------------------------")

print("Read data from CSV and format output as following:\n")
ReportData = pd.read_csv("TestingFile.csv")
# print(ReportData)

for i in range(len(ReportData)):
    print(ReportData.iloc[i,0],'->',ReportData.iloc[i,0],'->',ReportData.iloc[i,3])
print("--------------------------------")