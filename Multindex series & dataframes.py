import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# SERIES IS 1D AND DATAFRAMES ARE 2D OBJECTS;
# CAN WE HAVE MULTIPLE INDEX ?LETS'S TRY;;
index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a=pd.Series([1,2,3,4,5,6,7,8],index=index_val)
print(a)

# THE SOLUTION-> MULTIINDEX SERIES ALSO KNOWN AS HIERARCHICAL INDEXING;
# HOW TO CREATE A MULTIINDEX OBJECTS?
# 1.PD.MULTINDEX.FROM_TUPLES();;
index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multi=pd.MultiIndex.from_tuples(index_val)
print(multi)
print(multi.levels[1])

# 2.PD.MULTINDEX.FROM_PRODUCT();;
print(pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]]))

# CREATING A SERIES WITH MUTLIINDEX OBJECTS;;
s=pd.Series([1,2,3,4,5,6,7,8],index=multi)   #2d
print(s)

# HOW TO FETCH ITEMS FROM SUCH A SERIES;;
print(s['cse'])
print(s['ece'])

# UNSTACK;;
temp=s.unstack()
print(temp)

# STACK;;
print(temp.stack())

# MULTINDEX DATAFRAME;;
branch1=pd.DataFrame(
    [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
    [11,12],
    [13,14],
    [15,16],
],

index=multi,
columns=['avg_package','students']
)
print(branch1)
print(branch1.loc['cse'])
print(branch1['avg_package'])

# MULTINDEX DF FROM COLUMNS;;
branch=pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index=[2019,2020,2021,2022],
    columns=pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
print(branch)
print(branch['delhi'])
print(branch['mumbai'])
print(branch.loc[2019])

# STACKING AND UNSTACKING;;
print(branch1.unstack().unstack())

# WORKING WITH MULTIINDEX DATAFRAMES;;
# HEAD AND TAIL;;
print(branch1.head())
print(branch1.tail())
print(branch1.info())
print(branch1.shape)
print(branch1.duplicated())
print(branch1.isnull())

# EXTRACTING FROM A SINGLE ROW;;
print(branch1.loc['cse',2022])

# MULTIPLE;;
print(branch1.loc[('cse',2019):('ece',2020):2])

# USING ILOC;;
print(branch1.iloc[0:5:2])    #through indexing

# EXTRACTING COLUMNS;;
print(branch['delhi']['students'])
print(branch.iloc[:,1:3])

# SORT_INDEX;;BASED ON ONE LEVEL
print(branch1.sort_index(ascending=False))
print(branch1.sort_index(level=0,ascending=[False]))
# TRANSPOSE;;
print(branch1.transpose())
print(branch1.swaplevel())

# MELT ->WIDE TO LONG;;
print(pd.DataFrame({'cse':[120]}).melt())

# MELT BRANCH WITH YEAR;;
print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[210]}).melt(var_name='branch',value_name='num_student'))

df=pd.DataFrame({
    'branch':['cse','ece','mech'],
    '2020':[100,109,200],
    '2021':[120,20,10],
    '2022':[150,120,22]
}
)
print(pd.melt(df,id_vars=['branch'],var_name='year',value_name='students'))

# MELT REAL WORLD EXAMPLE;;
deaths=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\time_series_covid19_deaths_global.csv')
covid=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\time_series_covid19_confirmed_global.csv')
print(deaths.head(4))
print(deaths.shape)
print(covid.head())

deaths=deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_deaths')
covid=covid.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')
print(deaths)
print(covid)
print(covid.merge(deaths,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','num_deaths']])
