# War-in-Ukraine-dev
About:

The War in Ukraine has started on February 24th, 2022. And as the person that comes from Russia and lives abroad, I have access to multiple resources unlike people who live in Russia and only have access to the propaganda that the government creates. In this analysis, I wanted to see the the ongoing effects of the war and how it is covered in the news and social media. It is also important to note, that because the war is still going on, the data is limited and does not show the full impact.

Data:
My data is coming from multiple sources. First, I have data that was collected by multiple agencies such as the Ukraine Ministry of Defense, and international non-profits that have looked at the events that have taken place in Ukraine since the start of the war which was February 24th, 2022. They look at the events reported in the news, and categorized it into the losses section for equipment and personnel. The data could be found on  : 
https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war
Losses of equipment: https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/russia_losses_equipment.csv.zip
Losses of personnel: https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/russia_losses_personnel.csv.zip
My second dataset is also found on  which is a collection of all the Twitter tweets over time since the start of the war: https://www.kaggle.com/code/ssaisuryateja/eda-and-sentiment-analysis/data. Here I used all of the tweets from these 3 days: March 2nd, April 1st and April 20th
https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/0401_UkraineCombinedTweetsDeduped.csv.zip
https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/0420_UkraineCombinedTweetsDeduped.csv.zip
https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/UkraineCombinedTweetsDeduped_MAR02.csv.zip
The third dataset is from Github, which looks at the events reported that were mentioned in different news channels(both Ukrainian and international news that have mentioned anything relevant to the war in Ukraine): https://github.com/zhukovyuri/VIINA/blob/master/README.md
The datasets are control_latest1.csv.zip and events_latest.csv.zip
I have also used the twitter yaml to get the security tokens for the API twitter analysis: https://github.com/lymenbae/War-in-Ukraine-dev/blob/main/twitter_config.yaml

The Process:
First, the tweets.py file should be read which will look at the analysis of all of the tweets on March 2nd, April 1st and April 20th, and it would show how over time the reaction to Ukraine has changed and what prevalence does it have in the social media.
Then, looking at the BBC World and NY Times analysis file, we could see how Twitter was covered in these news channels on twitter in mid-april, and what is the sentiment of the coverage of the news.
The last two files: clean data and graphing.py look at the losses that Russia has experienced by producing multiple visualizations, which make it easier and much more efficient to see the impact of the war.

Results:

Using the seaborn graphing package, I analyzed the losses that Russia has experienced over the first 50 days of the war.
In regards to the soldiers lost, Russia has lost nearly 19,000 soldiers: 

![Line plot showing the number of Russian soldiers dead](Number%20of%20Russian%20soldiers%20lost.png)

Number of Prisoners of War was nearly 500 in first 50 days: 

![Line plot showing the amount of prisoners of war](Russian%20Prisoners%20of%20War%20in%20Ukraine.png)

Russia has lost a lot of its equipment: 

![Line plot showing the equipment lost](correct%20figure%20for%20the%20equipment%20loss.png)

The code in the file clean data provides more analysis where all of the types of the equipment are grouped together by the category and shown in a table.

I have also ran some analysis, looking at the correlations between the prisoners of war and equipment lost:

![Bar plot showing the correlations of losses between equipment and prisoners of war](POW%20and%20Equipment%20Loss%20Correlation.png)

And finally, I looked at the comparison of the growing number of prisoners of war vs the total amount on a daily basis: 

![Line plot looking at the daily increase of prisoners of war vs the total amount](Daily%20increase%20of%20Prisoners%20of%20war.png)

Then, using the QGIS, I have mapped the territory of Ukraine, looking at these 3 dates: February 27th, March 27th, and May 2nd., and looking how the fighting and control of the territories has advanced over time. The dark blue shows the territory under the control of Ukraine, purple is Russia, and green are contested areas, where yellow indicates that it is still under question (not enough data collected yet).

February 27th:

![Map of Ukraine showing which parts of the country in Ukraine are under whose control as of February 27th](Map%20of%20UA%202_27.png) 

March 27th:

![Map of Ukraine showing which parts of the country in Ukraine are under whose control as of March 27th](map%20of%20UA%203_27.png) 

April 27th: 

![Map of Ukraine showing which parts of the country in Ukraine are under whose control as of April 27th](map%20of%20UA%204_27.png)

May 22nd:

![Map of Ukraine showing which parts of the country in Ukraine are under whose control as of May 22nd](map%20of%20UA%205_22.png)

Looking into more in depth, to see in more detail using the pie charts to show under what percentage of control different parts of Ukraine are in. 
Yellow shows contested areas, green reflects the missing data, light purple is under Russian control, and blue is under Ukrainian control.

February 27th:

![](right%2027%2002%20pie%20charts.png)

March 27th:

![](fighting%20areas%2027%2003.png)

April 27th:

![](fighting%20areas%2024%2007.png)

May 22nd:

![](22%2005%20fighting%20areas.png)

June 5th:

![](fighting%20areas%2005%2006.png)

Based on this analysis, it could be seen that Russia has gained a lot of control over the Eastern part of Ukraine which is the most disputed territory, and most of the fighting is now done there, because Russia wants to have a total control over them, and actually it did approve the legitimacy and independence of the two provinces there: Luhansk and Donetsk.
Lastly, looking at the twitter and news analysis, I have found that BBC World and NY Times had 13% and 12% of their coverage respectfully focusing on the war in Ukraine. And the sentiment analysis looking at these two news channels in Twitter, it was either super low or negative, meaning that attitudes towards the war are mostly negative even among the official news channels.
Overall, looking at the analysis of Twitter as the social media, the majority of the hashtags have been related to the War in Ukraine: 

![Bar plot looking at what were the most popular hashtags on Twitter](correct%20version%20of%20hashtags%20over%20time.png)


