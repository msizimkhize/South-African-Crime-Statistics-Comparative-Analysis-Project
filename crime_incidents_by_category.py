import pandas as pd

#load the dataset
df = pd.read_csv("crime_incidents_by_category.csv")
df.head(15)

#filter rows based on location
df[df["Geography"] == "ZA"]
df.head(15)

#we derive a new useful dataset
df[df["Geography"] == "ZA"].to_csv("crime_incidents_za.csv")

#we now establish the new data frame
df2 = pd.read_csv("crime_incidents_za.csv")
df2.head(15)

#filter out null values
df2[df2.notnull()].head(15)
df2[df2.notnull()].to_csv("crime_incidents_za.csv")

#We further filter the data based on crime category
df2[df2["Crime Category"] == "Other Serious Crimes"].head(15)
df2[df2["Crime Category"] == "Other Serious Crimes"].to_csv("crime_incidents_za.csv")

#we update the dataframe df2
df2 = pd.read_csv("crime_incidents_za.csv")

#we finally select the columns of special interest
df2[["Crime Category", "Count"]].to_csv("crime_incidents_za.csv")

#we update the dataframe df2
df2 = pd.read_csv("crime_incidents_za.csv")

#we preview the dataframe df2
df2.head(15)