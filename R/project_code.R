install.packages("readr", dependencies = TRUE)
install.packages("dplyr", dependencies = TRUE)

library(readr)
library(dplyr)

crime_incidents_by_category <- read_csv("Downloads/crime_incidents_by_category.csv")
df1 <- crime_incidents_by_category %>%
 filter(Geography == 'ZA')

head(df1, 12)