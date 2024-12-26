# South African Crime Statistics — Comparative Analysis Project

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

The data presented as a CSV is accessible and credible: R Studio was used for the purpose of tabulating it.

The data is provided on the South African crime statistics between the year 2011 and 2023. The parameters, by criterion, will be tabulated in this report, based on the nature and demographics of the crime.

The data was processed as follows, so as to yield the desired visuals and information.
***
### I) The data is tabulated annually against the category of the criminal offense (R-Studio)

In R Studio, we observe the categorically South African crimes

```
library(readr)

crime_incidents_by_category <- read_csv("Downloads/crime_incidents_by_category.csv")
View(crime_incidents_by_category) 
```

![](https://github.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/raw/refs/heads/main/R%20Studio/1_uyEXe9u6BuJDCbXntketKQ.webp)
***
### II) The dataset is visualised over the entire span of the 2011–2023 term (**Tableau**)

![](https://github.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/raw/refs/heads/main/Tableau/1_mhBaXiczppWcKm6kfXsUog.webp)

![](https://github.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/raw/refs/heads/main/Tableau/1_6GeFBiJhKD6OGksRE1rSYw.webp)
***
## Insights and Conclusion

A comprehensive observation of the data reveals that serious crimes, of which human trafficking is implicated, are of the greatest contributors toward crime in South Africa. Overall, these numbers have remained rather steady, with a mild decline toward the latter phase.

Coupled with my experience in Statistics South Africa, as well as pure mathematics being my major, I would estimate that human trafficking remains a threat to South Africans, and is a severely under-reported event. South Africans who are more at risk to fall prey to this crime should be educated on ways to avoiding falling victim to abductions, and encouraged to report such crimes in their neighborhoods, knowing that all criminal reports are handled with utmost confidentiality.
***
### Reach Out on LinkedIn

[![](https://raw.githubusercontent.com/msizimkhize/-South-African-Crime-Statistics-Comparative-Analysis-Project/1f3d9ebec740ae97c9ac54fcd63315042bd8cc68/IMG/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d436f6e6e6563742d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e.svg)](https://www.linkedin.com/in/msizimkhize/)
