# Surfs Up
Weather analysis with Python

## Overview
I am looking to move to Hawaii to open a Surf & Ice Cream Shop. To help fund this venture, I began looking for investors. One investor in particular, W. Avy was interested, but having had a similar failed venture in the past, he asked me to do some analysis of the weather of the particular Island, Oahu, I'm looking to open the shop on. Using Python, Pandas methods and SQLAlchemy, I filtered the data to determine whether the weather would be hospitable enough to successfully run a Surf & Ice Cream Shop. 

## Results
After filtering and analyzing the data, I found the following differences between the June and December weather data: 

* Average Temperature: The difference between the average temperatures in June vs. December was only three degrees.
* Maximum Temperature: The difference between the maximum temperature in June vs. December was only two degrees.
* Minimum Temperature: The lowest temperature in December was significantly less (8 degrees) than in June as compared to the average and max temperature differences. 
* Rainfall: There was overall less total inches of rain in December than June, but December had much heavier rains with a higher max rainfall. 
* Reasonable Temperatures: Over 75% of the temperatures in both June and December were higher than 71 degrees. 

I pulled this data from the following summary statistics for June and December.  

![June Temperatures](https://github.com/jmmadson/surfs_up/blob/main/Resources/June_Temps.png?raw=true) ![December Temperatures](https://github.com/jmmadson/surfs_up/blob/main/Resources/Dec_Temps.png?raw=true)

The rain observation mentioned was pulled from my additional queries within the summary below. 


## Summary:

After analyzing the weather data from Oahu, Hawaii, I feel confident that a Surf & Ice Cream shop would do well and would be a good investment. 

With the average and high temperatures being so close between June and December, it can be inferred that the temperature is consistently reasonable for year round surfing. While there is a much larger difference between the low temperature in December, for both months, over 75% of the temperatures recorded were over 71 degrees - perfect for surfing and ice cream treats! 

In addition to looking at temperature, I ran two additional queries to determine the rainfall for both June and December. While June is definitely rainer than December, December did have heavier rainfalls overall. Those queries are available for review below: 

![June Query](https://github.com/jmmadson/surfs_up/blob/main/Resources/June_Query.png?raw=true)
![December Query](https://github.com/jmmadson/surfs_up/blob/main/Resources/Dec_Query.png?raw=true)

If W. Avy would like me to do additional analysis I would run queries to look for the following: 
* The actual and average number of days within June and December that had rainfall to further determine days the shop could be open for business. 
* The station that reported the most consistent highest temperature and lowest rainfall, to determine the best location for the shop. 
