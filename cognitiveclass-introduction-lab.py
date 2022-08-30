# -----------------------
# CognitiveClass.ai | IBM: DA0101EN "Data Analysis with Python" | Introduction Notebook (Lab 1) script notes
# Created by Elyzza Bobadilla for Python github repository
# Original by Joseph Santarcangelo for IBM Developer Skills Network
# Contents:
# Data Acquisition
# Basic Insight of Dataset
# -----------------------

# import pandas and numpy libraries
import pandas as pd
import numpy as np

# path of the dataset's location
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

# read the online file by the URL provided, and assign it to variable "df"
df = pd.read_csv(path, header = None) # the dataset doesn't have headers
# pandas automatically sets the first row as a header otherwise so must declare if dataset does not have a header

# check the top n rows of the dataframe, where n is an integer, with dataframe.head(n)
df.head(5)

# Q1: check the last n rows of the dataframe with dataframe.tail(n)
df.tail(10)


# to add headers to a dataset without headers: 1) create a list of header names, 2) assign list to columns
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
# returns
#headers
# ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base',
# 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio',
# 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']


# replace headers and check dataframe
df.columns = headers
df.head(10)

# must replace the "?" symbol with NaN so the dropna() can remove the missing values
df1=df.replace('?',np.NaN)

df=df1.dropna(subset=["price"], axis=0) # drop missing values along the column 'price'
df.head(20)


# Q2: find the name of the columns of the dataframe
print(df.columns)

# to save the dataset as a csv, use dataframe.to_csv()
df.to_csv("automobile.csv", index=False) # first argument is the file path & name, second means the row names will not be written


# Read/Save Other Data Formats
#Data Format	Read    	Save
#csv	    pd.read_csv()	df.to_csv()
#json	    pd.read_json()	df.to_json()
#excel	    pd.read_excel()	df.to_excel()
#hdf	    pd.read_hdf()	df.to_hdf()
#sql	    pd.read_sql()	df.to_sql()


# run dataframe.dtypes to see the names of columns and their data types
df.dtypes

# use dataframe.describe() to get a statistical summary of numeric attributes, e.g., count, column mean value, column standard deviation; excludes NaN (Not a Number) Values
df.describe()

# include all to check all columns including the ones with object data type
df.describe(include = "all")


# Q3: Question #3: You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3']]
# Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3'] ].describe()
# Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.
df[['length','compression-ratio']].describe()

# dataframe.info() provides a concise summary; this method prints information about a dataframe including the index datatype and columns, count of non-null values, and memory usage
df.info()

