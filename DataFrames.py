import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]

#Define dataframe
df = pd.DataFrame(data = [A,B,C,D,E],index = ['a','b','c','d','e'], columns = ['W', 'X', 'Y', 'Z'])
print("DataFrame:\n\n", df,"\n")
print("Print element from first column and first row: ",df['W'][0])