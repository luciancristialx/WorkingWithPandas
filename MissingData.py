import numpy as np
import pandas as pd

dictionary={'a':[1,2,3,4,5],'b':[6,7,8,9,np.NAN],'c':[0,1,2,np.NAN,np.NAN],'d':[3,4,np.NAN,np.NAN,np.NAN],'e':[5,np.NAN,
                                                                                                       np.NAN,np.NAN,np.NAN]}
print("Dictionary:\n",dictionary,"\n--------------------------------\n")

#Convert to dataframe
df=pd.DataFrame(dictionary)
print("DataFrame:\n",df,"\n--------------------------------\n")

#Remove rows with missing values on axis 0
# print("Remove rows with missing values on axis 0:\n",df.dropna(axis=0),"\n--------------------------------\n")

#Remove rows with missing values on axis 1
# print("Remove rows with missing values on axis 1:\n",df.dropna(axis=1),"\n--------------------------------\n")

#Replace missing values with certain value
# print("Replace missing values with certain value:\n",df.fillna(1),"\n--------------------------------\n")

#Replace missing values on a specific column with the average
print("Replace missing values on a specific column with the average\n",df['b'].fillna(value = df['b'].mean()),
    "\n--------------------------------\n")







