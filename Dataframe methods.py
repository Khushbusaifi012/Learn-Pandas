#SOME IMPORTANT FUNCTIONS;;
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# value_counts(series and dataframe);;
marks=pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
print(marks)
print(marks.value_counts())

ipl=pd.read_csv('ipl-matches.csv')    #importing file
print(ipl.head(5))

# FIND WHICH PLAYER HAS WON MOST MOM -->I FINALS AND QUALIFIERS;
ipl=pd.read_csv('ipl-matches.csv')
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

# TOSS DECISION PLOT;
print(ipl['TossDecision'].value_counts().plot(kind='pie'))
plt.show()

# HOW MANY MATCHES EACH THEM HAS PLAYED;;
print(ipl['Team1'].value_counts()+ipl['Team1'].value_counts().sort_values(ascending=False))

# SORT_VALUES()   (SERIES AND DATAFRAMES);;
x=pd.Series([1,2,3,4,5])
print(x.sort_values(ascending=False))
movies=pd.read_csv('movies.csv')
print(movies.head())
print(movies.sort_values('title_x',ascending=False))
print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))

# RANK(SERIES);;
batsman=pd.read_csv('batsman_runs_ipl.csv')
print(batsman.head())
batsman['batting_rank']=batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))

# SORT_INDEX(SERIES AND DATAFRAMES);;
marks={
    'maths':56,
    'english':78,
    'science':90,
    'hindi':100
}
marks_series=pd.Series(marks)
print(marks_series)

print(marks_series.sort_index(ascending=False))
print(movies.sort_index(ascending=False))

# SET_INDEX(DATAFRAME);;;
print(batsman.set_index('batter',inplace=True))

# RESET_INDEX(SERIES+DATAFRAME);;
print(batsman.reset_index(inplace=True))

# HOW TO REPLACE EXISTING INDEX WITHOUT LOOSING;;
print(batsman.reset_index().set_index('batting_rank'))

# SERIES TO DATAFRAME USING RESET_INDEX;;
print(marks_series.reset_index())

# RENAME(DATAFRAME);;
print(movies.rename(columns={'imdb_id':'id','poster_path':'link'}))

# UNIQUE(SERIES);;
temp=pd.Series([1,2,3,4,5,6,6,7,8,8,8,8,2,1,1,1,np.nan,np.nan])
print(temp)
print(temp.unique())

# NUNIQUE(SERIES+DATAFRAME)DOES NOT COUNT NAN OPERATOR;;
print(len(ipl['Season'].unique()))
print(ipl['Season'].nunique())

# ISNULL(SERIES+DATAFRAME);;
print(movies['title_x'].isnull())

# # NOTNULL(SERIES+DATAFRAME);;
print(movies['title_x'].notnull())

# # HASNANS(SERIES+DATAFRAME);;
print(marks_series.hasnans)

# # DROPNA(SERIES+DATAFRAME);;
print(movies.dropna())

# # FILLNA(SERIES+DATAFRAME);;
print(movies.fillna(0))

# DROP_DUPLICATES(SERIES+DATAFRAME);;
print(marks.drop_duplicates())

# # FIND THE LAST MATCH PLAYED BY VIRAT KOHLI IN DELHI;;
ipl['all_players']=ipl['Team1Players']+ipl['Team2Players']
print(ipl.head())

def did_kohli_play(players_list):
    return 'V Kohli' in players_list

ipl['did_kohli_play']=ipl['all_players'].apply(did_kohli_play)
ipl[(ipl['City']=='Delhi') & (ipl['did_kohli_play']==True).drop_duplicates()]

# DROP(SERIES+DATAFRAME);;
print(movies.head())
print(movies.drop(columns=['title_x']))
print(movies.drop(index=[0,9]))

# APPLY(SERIES+DATAFRAME);;
temp=pd.Series([10,20,30,40,50])
def sigmoid(value):
    return 1/1+np.exp(-value)
print(temp.apply(sigmoid))

# APPLY SECOND EXAMPLE;;
points_df = pd.DataFrame(
    {
        '1st point': [(3, 4), (-8, 9), (0, 0), (4, 5)],
        '2nd point': [(-3, 4), (0, 0), (2, 2), (10, 10)]
    }
)

print(points_df)

def euclidean(row):
    pt_A = row['1st point']
    pt_B = row['2nd point']
    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5
print(points_df.apply(euclidean,axis=1))