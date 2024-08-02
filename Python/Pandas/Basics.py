####  Welcome to Python Pandas Library 
### Pandas Data Structures
##SERIES -- > Similar to numpy array but series can be accessed by axis labels (Indexes)
# Series is One dimensional labelled array, supports multi data type      

import pandas as pd  #Create pandas series from a list
my_list = [10,20,30]  #Define the list and add values
series = pd.Series(my_list) #Convert list to series
print(series)               #Print the series
print(series.index)         #Print the index
print(series.values)        #Print the values

my_dict = {'Key1': 1, 'Key2' : 2, 'Key3': 3 }  #Create Pandas Series from Dictionary
ser = pd.Series(my_dict)
print(ser)
print(ser.index)
print(ser.values)

import pandas as pd       #Access the values using indexes 
ser1 = pd.Series([1,2,3,4], index=['USA','Germany','France','India'])
ser2 = pd.Series([1,2,3,4], index=['USA','Germany','France','India'])
print(ser1['USA'])        # Find the Value of USA using index 
print (ser1)
print(ser2)
print(ser1 + ser2)   #Add or combine
print(ser1/ser2)     #Divide 

##DataFrame-->  Way to store data in rectangular grids that can be easily overviewed
#Two dimensional labelled array, supports multiple data types  
import pandas as pd
import numpy as np 
df = pd.DataFrame([[1,2,3],
                   [3,4,5],
                   [5,6,7],
                   [7,8,9]])
print(df)
print(type(df))   #Prints the data type of variable 
print(df.shape)   #Print the Number of rows and colums (4,3)
print(df.index)   #Prints Index Information

# Index Accessing 
import pandas as pd  
df2 = pd.DataFrame([[1,2,3],[3,4,5],[5,6,7],[7,8,9]],
                   index = ['a','b','c','d'], columns= ['x','y','z'])
print(df2)
print(df2.index)
print(df2.shape)
print(df2.info)
print(df2.describe)
print(df2.max)
print(df2['x'] + df2['y'] + df2['z'])
print(df2['z'])
print(df2['z'].max)

# A project on Data Weather Set  to understand Pandas Function and Transformations
import pandas as pd
df = pd.read_csv('/Users/Vivek/Downloads/python-for-data-engineering-main/4. Python Advance/data/weather_2012.csv') 
print(type(df['Date/Time']))
print(df['Date/Time'].head(5)) # Select the Date/Time column and print first 5 rows.
print(type(df['Date/Time']))   #Print the data type of selected column (REMEMBER A SINGLE COLUMN IS A SERIES)
# Pandas is throwing Date/Time as an object, it is not understanding the type of column selected, hence we specify it to pandas that it is a date time type
# Lets Convert Date/Time column from object to timestamp, so that we can extract the month or perform date time functions 

import pandas as pd
df = pd.read_csv('/Users/Vivek/Downloads/python-for-data-engineering-main/4. Python Advance/data/weather_2012.csv') 
df['Date/Time'] = pd.to_datetime(df['Date/Time'])  # Object to Datetime (Timestamp)
print(type(df['Date/Time']))
print(df['Date/Time'])
print(df.info)
print(df['Date/Time'].unique()) #Unique Values 
print(df['Wind Spd (km/h)'].unique())  #Unique Wind Speed Values 
print(df['Wind Spd (km/h)'].nunique()) # count of unique value 
print(df['Weather'].value_counts()) #Count of values 
