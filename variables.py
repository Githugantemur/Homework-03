
# list (tuple, set)

my_list = [1,2,3,4,5]
my_str_list = ['a', 'b', 'c', 'd', 'e']
my_mix_list = [1, 'a', 2, 'b', 3, 'c']  

# slicing
my_list[0] # 1st
my_list[1] # 2nd
my_list[-1] # last
my_list[-2] # 2nd last
my_list[0:3] # 1st to 3rd
my_list[:3]
my_list[3:]
my_list[3:10]
my_list[-3:]


# append a list
my_list = my_list + [6,7,8,9,10]
my_list = my_list + 11
my_list = my_list + [11]
my_list.append(12)
my_list.append([13,14,15])
my_list.extend([13,14,15])



# delete
del my_list[-4]

# assign 
my_list[1] = 1.5
type(my_list)

# tuple 
my_tuple = (1,2,3,4,5) # type(my_tuple)
my_tuple[1] = 1.5

# set
my_set = {1,2,3,3,4,5,5,5,5,5}
worker_set = {'John', 'Mary', 'Peter', 'John', 'Peter'}

my_list_as_set = set(my_list)
my_list_as_tuple = tuple(my_list)
my_tuple_as_list = list(my_tuple)

my_range = range(100)
my_range_as_list = list(my_range)


# dictionary
a_dict = {'name': 'Bat'}
bat_dict = {'name': 'Bat', 'age': 30, 'location': 'Khovd'}
bat_dict['age']
bat_dict['location']
tsetseg_dict = {'name': 'Tsetseg', 'age': 25, 'location': 'Dornod'}
tsetseg_dict['name']
tsetseg_dict['location']

customer_dict = {'1': bat_dict, '2': tsetseg_dict}
customer_dict['2']['location']

anton_dict = {'name': 'Anton', 'age': 27, 'location': 'Moscow'}
customer_dict['3'] = anton_dict
customer_dict['3']['location']

bat_dict['income'] = 1000
customer_dict = {'1': bat_dict, '2': tsetseg_dict}
customer_dict['3'] = anton_dict

del customer_dict['1']['income']
customer_dict['1']['location'] = 'Ulaanbaatar'

customer_dict.keys()
bat_dict.keys()
customer_dict['1'].keys()
customer_dict['1'].values()



# datetime 
'19 Oct, 2024'
'2024-10-19'
'2024/10/19'

import datetime

now = datetime.datetime.now()
today = datetime.date(2025,4,19)
timenow = datetime.time(10,43)
first_date = datetime.date(2025,4,12)
today - first_date

today.year
today.month
today.day
now.year
now.hour
now.second
now.microsecond

# parse date
# https://strftime.org/
datetime.datetime.strptime('2024-12-05', '%Y-%d-%m')
datetime.datetime.strptime('2024/12/05', '%Y/%m/%d')
datetime.datetime.strptime('24/12/05', '%y/%m/%d')
datetime.datetime.strptime('05 Dec, 2024', '%d %b, %Y')


# format date to string
datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
my_date = datetime.date(2024,12,5)
datetime.datetime.strftime(my_date, '%y---%B---%d')

# timestamp
datetime.datetime.timestamp(now)

# from timestamp
datetime.datetime.fromtimestamp(1745052189)
datetime.datetime.fromtimestamp(1745052189+24*60*60)
datetime.datetime.fromtimestamp(1740215396-24*60*60)
datetime.datetime.fromtimestamp(0)



# pandas (dataframe), numpy
import pandas as pd
import os
os.getcwd()
# os.chdir('../..')

df = pd.read_excel('1_Introduction/data.xlsx')
# df = pd.read_excel('../../3_Data_cleaning/data.xlsx')

df.columns
df.index
df.head()
df.tail()
len(df) # number of rows
df.info()
df.dtypes
df.describe()

df['age']
df[['firstName','age']]
df['gender'].unique()
df['gender'].value_counts()
df['age'].max()
df['age'].min()


# filter
df[df['age'] > 27]
df[(df['age'] > 27) & (df['gender'] == 'M')]
df[(df['age'] > 27) & (df['gender'] == 'M')]['firstName']
df[(df['age'] > 27) & (df['gender'] == 'M')][['firstName','age','salary']]

# pivot, groupby
df.groupby('gender')['salary'].mean()
df.groupby(['gender','politicalView'])['salary'].mean()
df.groupby(['gender','politicalView']).agg({'salary': ['mean','max'], 'age': ['mean','min']})

pivot_table = pd.pivot_table(
    df, 
    values=['salary', 'age'], 
    index='gender', 
    columns='politicalView',
    aggfunc={'salary': ['mean', 'max'], 'age': ['mean', 'max']}
)

# date conversion, extract month
df['date'] = pd.to_datetime(df['startDate'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

df['date_str'] = df['date'].dt.strftime('%y/%m/%d')
df['date2'] = pd.to_datetime(df['date_str'], format='%y/%m/%d')


# if, loop

a = 10
b = 20
if a > b:
    print(f'{a} is greater than {b}')


if a > b:
    print(f'{a} is greater than {b}')
else: 
    print(f'{a} is not greater than {b}')


a = 20
b = 20
if a > b:
    print(f'{a} is strictly greater than {b}')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{a} is strictly less than {b}')

c = 15
if c > 10:
    print(f'{c} is greater than 10')
elif c > 5:
    print(f'{c} is greater than 5')
else:
    print(f'{c} is not greater than 5')

# loop

my_list = ['Bat','Dorj','Tsetseg','Anton']

for name in my_list:
    print(name)

for i in range(1000):
    print(i)


for i in range(1000):
    if i % 2 == 0:
        print(i)

# while loop

i = 0
while i <= 100:
    print(i)
    i += 1 # i = i + 1


# numpy
import numpy as np 

np_array = np.array([1,2,3,4,5])
np_array + 1

list(range(100))
rng = np.arange(10,100,5)
np.sin(rng)

# function
def add(a,b):
    return a + b

def add(a,b):
    c = a + b
    return c

def add(a,b):
    c = a + b
    print(f'sum of {a} and {b} is {c}.')
    return c

def add(a,b):
    c = a + b
    print(f'sum of {a} and {b} is {c}.')


# regex - regular expressions
# https://regex101.com/
import re

string = 'My phone number is +976-99119911, call me anytime.'
pattern = '\d{8}'

result = re.findall(pattern, string)
 
text = """
Hello from alice.smith@university.edu and 123john@badsite.xyz.
Also check admin@mail.google.com or john_doe42@company.org.
Invalid: .start@wrong.com or name@site.co.uk
"""

pattern = r'\b(?!\d)[a-zA-Z0-9](?:[a-zA-Z0-9._]*[a-zA-Z0-9])?@(?:[a-zA-Z0-9-]+\.)+(?:com|org|edu)\b'
matches = re.findall(pattern, text)
print(matches)