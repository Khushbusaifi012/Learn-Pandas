import numpy as np
import pandas as pd

# CREATING DATAFRAME;;USING LIST
student_data=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
print(pd.DataFrame(student_data,columns=['Iq','Marks','Package']))

# USING DICT;;
student_dict={
    'iq':[100,40,80],
    'marks':[80,90,100],
    'package':[90,100,80]
}
students=pd.DataFrame(student_dict)
print(students)

# USING READ_CSV;;;
movies=pd.read_csv('movies.csv')
print(movies)
ipl=pd.read_csv('ipl-matches.csv')
print(ipl)

# DATAFRAME ATTRIBUTES AND METHODS;;
movies=pd.read_csv('movies.csv')
print(movies.shape)   #shape
print(movies.dtypes)   #dtypes
print(movies.index)    #index
print(movies.columns)   #columns
print(movies.values)    #2d numpy array(values)
print(movies.head)      #head
print(movies.tail)      #tail
print(movies.sample(5))     #sample
print(movies.describe())    #describe
print(movies.info())      #info
print(movies.isnull())      #isnull
print(movies.duplicated().sum())       #duplicated
print(movies.rename(columns={'title':'Name'},inplace=True))     #rename

# MATH METHODS;;
ipl=pd.read_csv('ipl-matches.csv')
print(ipl.sum)  #sum
print(ipl.mean)   #mean
print(ipl.min)    #Min

# SELECTING COLS FROM A DATAFRAME;;
movies=pd.read_csv('movies.csv')       # SINGLE COLS;;
print(movies['title_x'])
print(type(movies['title_x']))   #series
                   
# MULTIPLE COLS;;
print(movies[['title_x','year_of_release','actors']])   #fancy indexing
print(type(movies[['title_x','year_of_release','actors']]))    #dataframe

# SELECTING ROWS FROM DATAFRAME;;
print(movies.iloc[0])   #iloc[single row]
print(movies.iloc[0:5])      #multiple rows
print(movies.iloc[[0,4,5]])    #fancy indexing

student_dict={
    'name':['khushbu','ankit','rupesh','amit','ankita'],
    'iq':[100,20,30,40,40],
    'marks':[80,80,90,100,12],
    'package':[10,7,14,2,0]
}
students=pd.DataFrame(student_dict)
students.set_index('name', inplace=True) # Set 'name' as the index
print(students)
print(students.loc['khushbu':'ankit'])   # Now you can access using loc(fancy indexing)
print(students.loc['rupesh':'amit'])

# SELECTING BOTH ROWS AND COLS;;
print(movies.iloc[0:3,0:3])

# FILTERING A DATAFRAME;;
# find all the final winners?
ipl=pd.read_csv('ipl-matches.csv')
print(ipl.head(10))
mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]
print(new_df[['Season','WinningTeam']])

# how many super over finishes have occured?
print(ipl[ipl['SuperOver']=='Y'].shape[0])

# how many matches has csk won in kolkata?
print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# toss winner in match winner in percentage?
print(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0]*100)

# movies with rating higher than 8 and votes>10000?
movies=pd.read_csv('movies.csv') 
print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0])

# action movies with rating higher than 7.5?
mask1=movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask2=movies['imdb_rating']>7.5
print(movies[mask1 & mask2])

# ADDING NEW COLS;;
movies['Country']='India'   #completely new
print(movies.head())

# movies.dropna(inplace=True)
movies['lead actor'] = movies['actors'].str.split('|').apply(lambda x: x[0])   #from existing ones
print(movies['lead actor'])
print(movies.head())

# IMPORTANT DATAFRAME FUNCTIONS;;
ipl=pd.read_csv('ipl-matches.csv')
print(ipl.info())
ipl['ID']=ipl['ID'].astype('int32')   #astype
print(ipl.info())