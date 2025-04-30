import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies=pd.read_csv('imdb-top-1000.csv')
print(pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\imdb-top-1000.csv'))
# print(movies.head())

# APPLYING BUILTIN AGGREGATION FUNCTIONS ON GROUPBY OBJECTS;
genres=movies.groupby('Genre')
print(genres)
print(genres.sum())
print(genres.min())

# FIND THE TOP THREE GENRES BY TOTAL EARNING;;
print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))

# FIND THE GENRE WITH HIGHEST AVERAGE IMDB RATING;;
print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# FIND DIRECTOR WITH MOST POPULARITY;;
print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

# FIND THE HIGHEST RATED MOVIE OF EACH GENRE;;
print(movies.groupby('Genre')['IMDB_Rating'].max())

# FIND NUMBER OF MOVIES DONE BY EACH ACTOR;;
print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

# GROUPBY ATTRIBUTES AND METHODS;;
# FIND TOTAL NUMBER OF GROUPS;;;
print(len(movies.groupby('Genre')))

# FIND ITEMS IN EACH GROUPS ->SIZE;;
print(movies.groupby('Genre').size())

# FIND FIRST AND LAST NTH ITEMS;;
print(movies.groupby('Genre').first())
print(movies.groupby('Genre').last())
print(movies.groupby('Genre').nth(5))

# GET GROUP VS FILTERING;;
print(genres.get_group('Horror'))

# GROUPS;;
print(genres.groups)
print(genres.describe())
print(genres.sample(2,replace=True))
print(genres.nunique())

# AGG METHOD;;PASSING DICT;;
print(genres.sum())
g=genres.agg({
    'Runtime':'mean',
    'IMDB_Rating':'mean',
    'No_of_Votes':'sum',
    'Gross':'sum',
    'Metascore':'min'
})
print(g)

# SPLIT(APPLY)COMBINE;;
print(genres.apply(min))

# FIND RANKING OF EACH MOVIE IN THE GROUP ACCORDING TO IMDB SCORE;;
def rank_movie(group):
    print(group['IMDB_Rating'].rank(ascending=False))
    return group
print(genres.apply(rank_movie))

# FIND NORMALIZED IMDB RATING GROUPWISE;;
def normal(group):
    group['norm_rating']=group['IMDB_Rating']-group['IMDB_Rating'].min()/group['IMDB_Rating'].max()-group['IMDB_Rating'].min()
print(genres.apply(normal))

# GROUPBY ON MULTIPLE COLS;;
duo=movies.groupby(['Director','Star1'])
print(duo)
print(duo.size())
print(duo.get_group(('Aamir Khan','Amole Gupte')))

# FIND THE MOST EARNING ACTOR DIRECTOR COMBO;;
print(duo['Gross'].sum().sort_values(ascending=False).head(1))

# FIND THE BEST IN TERMS OF METASCORE(AVG) ACTOR GENRE COMBO;;
print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False))

# EXCERCISE;;
ipl=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\deliveries.csv')
print(ipl.head(10))
print(ipl.shape)

# FIND THE TOP 10 BATSMAN IN TERMS OF RUNS;;
print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

# FIND THE BATSMAN WITH MAX NO OF SIXES;;
six=ipl[ipl['batsman_runs']==6]
print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])

# FIND BATSMAN WITH MOST NUMBER OF 4'S AND 6'S IN LAST 5 OVERS;;
team=ipl[ipl['over']>15]
team=team[(team['batsman_runs']==4) | (team['batsman_runs']==6)]
print(team.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])

# FIND V KOHLI RECORD AGAINST ALL TEAMS;;
team=ipl[ipl['batsman']=='V Kohli']
print(team.groupby('bowling_team')['batsman_runs'].sum().reset_index())

# CREATE A FUNCTION THAT CAN CREATE RETURN THE HIGHEST SCORE OF ANY BATSMAN;;
def highest(batsman):
    team=ipl[ipl['batsman']==batsman]
    print(team.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0])
highest('CH Gayle')