import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# SERIES FROM LISTS;;
country=['India','Pakistan','USA','Nepal','Srilanka']   #string
print(pd.Series(country))

run_series=[12,23,45,67,89,90]   #integer
print(pd.Series(run_series))

num=[12.4,78.9,100.0]    #float
print(pd.Series(num))

marks=[23,45,67,89,90]    #custom index
subjects=['maths','english','science','hindi','computer science']
print(pd.Series(marks,index=subjects))

# SETTING A NAME;;
print(pd.Series(marks,index=subjects,name="Khushbu's Marks"))

# SERIES FROM DICT;;
marks={
    'maths':67,
    'eng':57,
    'science':78,
    'hindi':90
}
marks_series=pd.Series(marks,name='khushbu marks')
print(marks_series)

#SERIES ATTRIBUTES;;
print(marks_series.size)   #size
print(marks_series.dtype)    #dtype
print(marks_series.name)    #name
print(marks_series.is_unique)   #is_unique
print(marks_series.index)    #index
print(marks_series.values)   #values

# SERIES USING READ_CSV;;with one col
df=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\subs.csv')
print(df.head(365))
print(type(pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\subs.csv')))    #it is in dataframe

# in converted to series;;
df=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\subs.csv')
series = df.squeeze()
print(type(series))   #it is in series

# WITH 2 COLS;; 
df=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\kohli_ipl.csv',index_col='match_no')
series = df.squeeze()
print(df.head(215))
print(type(series))

df=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\bollywood.csv',index_col='movie')
series=df.squeeze()    #squeeze
print(df.head(1501))
print(type(series))

# SERIES METHOD;;
# HEAD AND TALL;
subs = pd.read_csv('subs.csv')
print(subs.head())   #head

vk=pd.read_csv('kohli_ipl.csv')
print(vk.head(9))
print(vk.tail())    #tail
print(vk.sort_values)   #sort values

movies=pd.read_csv('bollywood.csv')
print(movies.sample(5))    #sample
print(movies.value_counts())    #value_counts
print(movies.sort_index)   #sort index

# SERIES MATH METHODS;;
vk=pd.read_csv('kohli_ipl.csv')
print(vk.count())   #count
print(vk.product())   #product
print(vk.median())    #median
print(vk.var())      #var

subs = pd.read_csv('subs.csv')
print(subs.sum())    #sum 
print(subs.mean())   #mean
print(subs.std())    #std
print(subs.min())    #min
print(subs.max())    #max
print(subs.describe())    #describe

movies=pd.read_csv('bollywood.csv')
print(movies.mode())    #mode

#SERIES INDEX SLICING;;
x=pd.Series([12,12,24,45,67,89,90])    #integer indexing
print(x[1])    #positive indexing
# print(x[-1])    #series not work in negative indexing

# SLICING;;
vk=pd.read_csv('kohli_ipl.csv')
print(vk[5:16])   #positive slicing
print(vk[-5:])    #negative slicing

# FANCY INDEXING;;
print(vk.iloc[[3, 4, 5, 6]])  

# EDITING SERIES;;USING INDEXING
marks={
    'maths':67,
    'eng':57,
    'science':78,
    'hindi':90
}
marks_series=pd.Series(marks,name='khushbu marks')
print(marks_series)
marks_series[1]=100
print(marks_series)

# # WHAT IF AN INDEX DOES NOT EXIST;;
marks_series['sst']=90
print(marks_series)

# SLICING;;
run_series=[12,23,45,67,89,90]   
print(pd.Series(run_series))
run_series[2:4]=[100,100]
print(run_series)
run_series[0] = 0    #fancy indexing
run_series[3] = 0
run_series[4] = 0
print(run_series)

# USING INDEX LABEL;;
movies=pd.read_csv('bollywood.csv')
movies['2 States (2014 film)']='Alia Bhatt'
print(movies)

# SERIES WITH PYTHON FUNCTIONALITIES;;
subs = pd.read_csv('subs.csv')
print(len(subs))   #len
print(type(subs))   #type 
print(dir(subs))    #dir
print(sorted(subs))   #sorted
print(subs.min())     #min
print(subs.max())     #max

# TYPE CONVERSION;;
marks={
    'maths':67,
    'eng':57,
    'science':78,
    'hindi':90
}
print(dict(marks))
print(list(marks))

# MEMBERSHIP OPERATOR;
movies=pd.read_csv('bollywood.csv')
print('Zindagi Tere Naam' in movies.values)   #In

# # LOOPING;;
for i in movies.index:
    print(i)   #looping

# ARITHMETIC OPERATOR;
print(100-marks_series)     #subtraction

# RELATIONAL OPERATOR;;;
vk=pd.read_csv('kohli_ipl.csv')
print(vk>=50)
print(vk<=100)

# BOOLEAN INDEXING ON SERIES;;
# # 1.FIND NO OF 50'S AND 100'S SCORED BY KOHLI?
vk=pd.read_csv('kohli_ipl.csv')
print(vk[vk<=50].size)

# FIND NUMBER OF DUCKS?
print(vk[vk>=0].size)

# COUNT NUMBER OF DAY WHEN I HAD MORE THAN 200 SUBS A DAY?
subs = pd.read_csv('subs.csv')
print(subs[subs>200].size)

# FIND ACTORS WHO HAVE DONE MORE THAN 20 MOVIES?
movies=pd.read_csv('bollywood.csv')
actor_counts = movies['lead'].value_counts()
popular_actors = actor_counts[actor_counts > 20]
print(popular_actors)

# PLOTTING GRAPH ON SERIES;;
subs = pd.read_csv('subs.csv')
print(subs.plot())
print(plt.show())

movies=pd.read_csv('bollywood.csv')
print(movies.value_counts().head(20).plot(kind='pie'))
print(plt.show())

vk=pd.read_csv('kohli_ipl.csv')
print(vk.plot())
print(plt.show())