import numpy as np
import pandas as pd

a = ['a','b','c','d','e']
b = [1,2,3,4,5]
c = {1:'a',2:'b',3:'c',4:'d',5:'e'}
d = pd.Series(data = a, index = b)
e = pd.Series(c)

print("---------\nSeries\n---------\nVersion1:\n",d,"\n")
print("Version2:\n",e)