import numpy as np
import pandas as pd

subs=pd.read_csv('subs.csv')
print(subs)

vk=pd.read_csv('kohli_ipl.csv')
print(vk)

movies=pd.read_csv('bollywood.csv')
print(movies)

#SOME IMPORTANT SERIES METHODS;;
import sys
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('int16')))   #astype

print(vk[vk["runs"].between(51, 90)].size)    #between

print(subs.clip(100,200))    #clip

#DROP DUPLICATES;;
temp=pd.Series([1,1,1,1,2,3,4,2,2,2])
print(temp)
print(temp.drop_duplicates())

temp=pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp) 
print(temp.isnull().sum())   #isnull
print(temp[~pd.isna(temp)])  #nan to remove invalid values
print(vk.isnull().sum())     #isnull
print(temp.fillna(temp.mean()))    #fillna

print(vk[vk["runs"].isin([49, 99])])   #isin

print(movies["lead"].apply(lambda x: x.split()[0].upper()))    #apply

new = vk.head().copy()   #copy
new.loc[1, 'runs'] = 100
print(new)
print(vk)