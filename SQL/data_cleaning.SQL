--Dataset is cleaned by clearing off null entries
DELETE FROM `crime-statistics-south-africa.crime_data.crime` WHERE Count='NULL';

--Dataset is cleared further by deleting all data entries made outside of the timeframe 2011-2023
DELETE FROM `crime-statistics-south-africa.crime_data.crime` WHERE 'Financial Year'> 2023 OR 'Financial Year' <2011;

--Data is selected as being representive of the national crime statistics
SELECT * FROM `crime-statistics-south-africa.crime_data.crime` WHERE Geography='ZA' LIMIT 1000;