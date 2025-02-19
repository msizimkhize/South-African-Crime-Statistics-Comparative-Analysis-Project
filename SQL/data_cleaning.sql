--Dataset is cleaned by clearing off null entries
DELETE FROM crime_data WHERE Count IS NULL;

--Dataset is cleared further by deleting all data entries made outside of the timeframe 2011-2023
DELETE FROM crime_data WHERE Financial_Year > 2023 OR Financial_Year < 2011;

--Data is selected as being representative of the national crime statistics
SELECT TOP 1000 * FROM crime_data WHERE Geography = 'ZA';
