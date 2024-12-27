# we first import needful packages
import numpy as np # data arrays
import pandas as pd # data structure and data analysis

# we read the CSV file
crimes = pd.read_csv("../Dataset/crime_incidents_by_category.csv")

# we get the sum of missing data points per column
missing_values_count = crimes.isnull().sum()
