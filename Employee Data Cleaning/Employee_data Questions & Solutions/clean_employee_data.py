import pandas as pd
import numpy as np

df=pd.read_csv('employee_data.csv',skipinitialspace=True)
#df=pd.read_csv(r"D:\Complete Python\Pandas Programming\employee_data.csv")
print(df.head().to_string())

#replace Nan,Null,inf/-inf values with Nan
df.replace(['inf','-inf','Nan','Null'],np.nan,inplace=True)

#check datatype of columns
print(df.dtypes)
print(df.columns)

#converting necessary data into floating data
df["Salary"]=pd.to_numeric(df["Salary"],errors='coerce')
df['Experience']=pd.to_numeric(df['Experience'],errors='coerce')
#df['Performance']=pd.to_numeric(df['Performance'],errors='coerce') #already in float64

#check datatype of columns
print(df.dtypes)

#count null values
print(df.isnull().sum()) #counts only actual Nan(np.nan), not string 'Nan'

#fill nan values of salary, experience, performance
'''
df['Salary']=df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['Performance']=df['Performance'].fillna(df['Performance'].median(),inplace=True)
df.fillna(df.mean(numeric_only=True),inplace=True) #fill every nan place with their cols mean
'''
#future enhancement
df[['Salary','Experience','Performance']]=df[['Salary','Experience','Performance']].fillna(df[['Salary','Experience','Performance']].mean())

#fill nan values of name, city & department
df[['Name','City','Department']]=df[['Name','City','Department']].fillna('Unknown')


#drop duplicates
df=df.drop_duplicates(subset=['Name','Age','Salary','Experience','City','Department','Performance'],keep='first')

#print values only 1decimal place
pd.set_option('display.float_format','{:,.1f}'.format)

#remove negative salaries
df['Salary']=np.where(df['Salary']<=0,df['Salary'].mean(),df['Salary'])

#handle outliners
sal_mean=df['Salary'].mean()
sal_std=df['Salary'].std()
lwr_bound=sal_mean-(3*sal_std)
upr_bound=sal_mean+(3*sal_std)
#remove salaries, where salary is too high or too low
df=df[(df['Salary']>=lwr_bound) & (df['Salary']<=upr_bound)]

print(df.head().to_string())
print(df.tail().to_string())

df.to_csv('cleaned_employee_data.csv',index=False)
print('Your file is successfully generated with name "cleaned_employee_data".')