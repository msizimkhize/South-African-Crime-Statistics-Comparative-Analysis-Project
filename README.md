# South African Crime Statistics: Comparative Analysis on Serious and Abduction-Related Crimes

![](https://github.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/blob/main/IMG/SAPS.png?raw=true)

***
## Abstract
This is an evaluation of the latest human trafficking reports per province, against the major contributors of crime in South Africa.

Alongside my vocational experience with Statistics South Africa, I was able to carry out the following investigation using South African Crime Statistics on Kaggle, R Studio, and Tableau.

The data was prepared:

- Zip folder containing dataset
- https://www.kaggle.com/datasets/harutyunagababyan/crime-stats-of-south-africa-2011-2023
- Latest crime statistics

The data is indeed limited, in that it only spans the eleven-year period. The data had to remain encrypted and entirely anonymous, as to ensure safety for the persons who reported the crimes herein contained.

The data presented as a CSV is accessible and credible: R Studio was used for the purpose of preprocessing it.

The data is provided on the South African crime statistics between the year 2011 and 2023. The parameters, by criterion, will be tabulated in this report, based on the nature and demographics of the crime.

The data was processed as follows, so as to yield the desired visuals and information.
***
### I) The data is tabulated annually against the category of the criminal offense

In R Studio, we browse and manually filter the categorically South African (ZA) crimes

```
library(readr)

crime_incidents_by_category <- read_csv("Downloads/crime_incidents_by_category.csv")
View(crime_incidents_by_category) 
```
|     |Geography|Crime Category|Financial Year|Count|
|-----|-----|-----|-----|-----|
|**501**|ZA|Other Serious Crimes|2011/2012|528296|
|**502**|ZA|Other Serious Crimes|2012/2013|517252|
|**503**|ZA|Other Serious Crimes|2013/2014|510748|
|**504**|ZA|Other Serious Crimes|2014/2015|499698|
|**505**|ZA|Other Serious Crimes|2015/2016|479075|
|**506**|ZA|Other Serious Crimes|2016/2017|469276|
|**507**|ZA|Other Serious Crimes|2017/2018|438113|
|**508**|ZA|Other Serious Crimes|2018/2019|444447|
|**509**|ZA|Other Serious Crimes|2019/2020|426569|
|**510**|ZA|Other Serious Crimes|2020/2021|354566|
|**751**|ZA|Other Serious Crimes|2021/2022|393821|
|**776**|ZA|Other Serious Crimes|2022/2023|437038|

The table is also obtained using the R code below.
```
install.packages("readr", dependencies = TRUE)
install.packages("dplyr", dependencies = TRUE)

library(readr)
library(dplyr)

df1 <- crime_incidents_by_category %>%
 filter (Geography == 'ZA')

head(df1, 12)
```

We now filter and clean the dataset using the following Python code

```
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
```

|     |Geography|Crime Category|Financial Year|Count|
|-----|-----|-----|-----|-----|
|**0**|ZA|Contact Crimes|2011/2012|615935|
|**1**|ZA|Contact Crimes|2012/2013|608724|
|**2**|ZA|Contact Crimes|2013/2014|611574|
|**3**|ZA|Contact Crimes|2014/2015|616973|
|**4**|ZA|Contact Crimes|2015/2016|623223|
|**5**|ZA|Contact Crimes|2016/2017|608321|
|**6**|ZA|Contact Crimes|2017/2018|601366|
|**7**|ZA|Contact Crimes|2018/2019|617210|
|**8**|ZA|Contact Crimes|2019/2020|621282|
|**9**|ZA|Contact Crimes|2020/2021|535217|
|**100**|ZA|Sexual Offences|2011/2012|60539|
|**101**|ZA|Sexual Offences|2012/2013|60888|
|**102**|ZA|Sexual Offences|2013/2014|56680|
|**103**|ZA|Sexual Offences|2014/2015|53617|
|**104**|ZA|Sexual Offences|2015/2016|51895|

```
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
```
|     |Unnamed: 0|Crime Category|Count|
|-----|-----|-----|-----|
|**0**|0|Other Serious Crimes|528296|
|**1**|1|Other Serious Crimes|517252|
|**2**|2|Other Serious Crimes|510748|
|**3**|3|Other Serious Crimes|499698|
|**4**|4|Other Serious Crimes|479075|
|**5**|5|Other Serious Crimes|469276|
|**6**|6|Other Serious Crimes|438113|
|**7**|7|Other Serious Crimes|444447|
|**8**|8|Other Serious Crimes|426569|
|**9**|9|Other Serious Crimes|354566|
|**10**|10|Other Serious Crimes|393821|
|**11**|11|Other Serious Crimes|437038|

```
#outliers are removed
df2[df2['Count'] < df2['Count'].quantile(0.99)]
df2.to_csv("crime_incidents_za.csv")

#we render a statistical summary
df2 = pd.read_csv("crime_incidents_za.csv")
df2[["Count"]].describe()
```

|     |Count|
|-----|-----:|
|**count**|12.000000|
|**mean**|458241.583333|
|**std**|52542.650605|
|**min**|354566.000000|
|**25%**|434420.750000|
|**50%**|456861.500000|
|**75%**|502460.500000|
|**max**|528296.000000|

***
### II) The dataset is visualised over the entire span of the 2011–2023 term (**Tableau**)

|Crime Category| |
|-----|-----:|
|**Aggrevated Robberies**|2,805,498|
|**Contact Crimes**|14,641,294|
|**Contact Related Crimes**|2,857,450|
|**Crimes Detected as a Result of Police Action**|7,564,641|
|**Other Serious Crimes**|10,997,798|
|**Property Related Crimes**|11,733,250|
|**Sexual Offences**|1,283,792|

![](https://github.com/msizimkhize/South-African-Crime-Statistics-Comparative-Analysis-Project/blob/main/IMG/1_6GeFBiJhKD6OGksRE1rSYw.png?raw=true)
***
## Insights and Conclusion

A comprehensive observation of the data reveals that serious crimes, of which human trafficking is implicated, are of the greatest contributors toward crime in South Africa. Overall, these numbers have remained rather steady, with a mild decline toward the latter phase.

Gicen the metric of serious crimes, over the fairly recent crime statistics, it is safe to conclude that human trafficking remains amongst the major threats to South Africans, and may be a severely under-reported event. South Africans who are more at risk to fall victims to this crime should be educated on ways to avoiding falling victim to abductions, and encouraged to report such crimes in their neighborhoods, knowing that all criminal reports are handled with utmost confidentiality. By consequence, what would have been a human traficking incident would become a crime combated by police action.

The category of 'other serious crimes' showed a decline of crime reports by a fairly constant gradient from the year 2011 to the year 2018. The crime reports continued falling linearly, before reaching a fair upward climb at the 2022/2023 timeframe.
***

![](https://github.com/msizimkhize/South-African-Crime-Statistics-Comparative-Analysis-Project/blob/main/IMG/F7379CRZGZ4Z.jpeg?raw=true)

### Reach Out on LinkedIn

[![](https://raw.githubusercontent.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/1f3d9ebec740ae97c9ac54fcd63315042bd8cc68/IMG/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d436f6e6e6563742d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e.svg)](https://www.linkedin.com/in/msizimkhize/)
