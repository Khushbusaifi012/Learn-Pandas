import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

courses=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\courses.csv')
print(courses.head(10))

students=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\students.csv')
print(students.head(10))

nov=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\reg-month1.csv')
print(nov.head(10))

dec=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\reg-month2.csv')
print(dec.head(10))

matches=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\matches.csv')
print(matches.head(10))

delivery=pd.read_csv(r'C:\Users\FARUKH KHAN\OneDrive\Desktop\CAMPUSX PANDAS\deliveries.csv')
print(delivery.head(10))

# CONCATENATION;;
print(pd.concat([nov,dec]))   #concat

# IGNORE_INDEX;;
reg=pd.concat([nov,dec],ignore_index=True)    #ignore_index
print(reg)

# MULTIINEX DATAFRAME;;
multi=pd.concat([nov,dec],keys=['Nov','Dec'])    #provided names
print(multi.loc['Dec'])
print(multi.loc['Nov'])      #loc which we want file
print(multi.loc[('Nov',2)])    #through index and loc
print(pd.concat(['nov','dec'],axis=1))    #if we want horizontally

# INNER JOIN;;
print(students.merge(reg,how='inner',on='student_id'))

# LEFT JOIN;;
print(courses.merge(reg,how='left',on='course_id'))

# RIGHT JOIN;;
temp=pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Khushbu','Ankit','bhupi'],
    'partner':[28,26,17]
})
students=pd.concat([students,temp],ignore_index=True)
print(students)

print(students.merge(reg,how='right',on='student_id'))
print(students.merge(reg,how='left',on='student_id'))

# OUTER JOIN;;
print(students.merge(reg,how='outer',on='student_id').tail(10))

# 1.FIND TOTAL REVENUE GENERATED;;
print(reg.merge(courses,how='inner',on='course_id')['price'].sum())

# 2.FIND MONTH BY MONTH REVENUE;;
temp=pd.concat([nov,dec],keys=['Nov','Dec']).reset_index()
print(temp.merge(courses,on='course_id').groupby('level_0')['price'].sum())

# 3.PRINT THE REGISTRATION TABLE COLUMNS-NAME-COURSE-PRICE;;
print(reg.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']])

#4. PLOT BAR CHART FOR REVENUE/COURSES;;
print(reg.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar'))
print(plt.show())

# 5.FIND STUDENTS WHO ENROLLED IN BOTH THE MONTHS;;
student_id=np.intersect1d(nov['student_id'],dec['student_id'])
print(students[students['student_id'].isin(student_id)])

# 6.FIND COURSE THAT GOT AN ENROLLMENT;;
course_id=np.setdiff1d(courses['course_id'],reg['course_id'])
print(courses[courses['course_id'].isin(course_id)])

# 7.FIND STUDENTS WHO DID NOT ENROLL INTO ANY COURSES;;
students_id_list=np.setdiff1d(students['student_id'],reg['student_id'])
print(students[students['student_id'].isin(students_id_list)])

# 8.PRINT STUDENT NAME PARTNER NAME FOR ALL ENROLLED STUDENTS;;
print(students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])    #SELF JOIN

# 9.FIND TOP 3 STUDENTS WHO DID MOST NUMBER ENROLLMENTS;;
print(reg.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))

# 10.FIND TOP 3 STUDENTS WHO SPENT MOST AMOUNT OF MONEY ON COURSES;;
print(reg.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3))

# ALTERNATIVE SYNTAX FOR MERGE;;
print(pd.merge(students,reg,how='inner',on='student_id'))

# IPL DATASET;;
# 1.FIND TOP 3 STADIUMS WITH HIGHEST SIXES/MATCHN RATIO?
temp=delivery.merge(matches,left_on='match_id',right_on='id')
six=temp[temp['batsman_runs']==6]
num_sixes=six.groupby('venue')['venue'].count()
num_matches=matches['venue'].value_counts()
print((num_sixes / num_matches).sort_values(ascending=False).head(10))

# 2.FIND ORANGE CAP HOLDER OF ALL THE SEASONS;;
print(temp.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates(subset=['season'],keep='first').sort_values('season'))