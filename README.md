# SeminarSD-ProjectAnilistAPI
Script that utilizes the AnilistAPI to fetch and visualize trending anime and their genres.

## About the Project
This was created as the project for the 202520 Sem in Advanced Software Dev CEN-4930C-24216 class.

If you are not familiar with Anilist, it is an anime and manga database, tracking, and social site. Its API utilizes GraphQL. You can read more about it here: https://docs.anilist.co/

### What does it do?
It is composed of two Python files. 
*AnilistProject* accesses the AnilistAPI, and fetches the top 10 trending anime at the time of the run, extracting the title, score, and genres. It then uses matplotlib to vizualize the trend of anime scores with a pink bar chart, and the frequency of anime genres with a blue bar chart. It will save both of these charts as well as the raw data it used to create them in designated folders (and it will create the folders in case you do not have them) with a descriptive name and timestamp. This file can be run as often as you like during the period of data collection.

Then, when the *aggregator* file is run, it will utilize the raw data saved to generate two frequency graphs: a dark pink bar graph for overall trending anime, and a dark blue bar graph for overall trending genres. It will also save these in a designated folder with a timestamp. That will aid with analysis and final conclusions after (or periodically thoroughout) your data collection.

**Examples of the generated data have been uploaded for demonstrative purposes**.

### To run: 
Should be very simple. You are welcome to download the entire folder, but you only need the two scripts. Once you open whichever script you want to run:
1. Install dependencies with: ```pip install requests matplotlib```
2. Run the script with: ```python script.py``` (so either ```python AnilistProject.py``` or ```python aggregator.py``` depending on which script you want to run.)

### Tools & Additional References
#### Tools:
This project was created with Python in VSCode, using the Anilist API, GraphQL, and matplotlib.
#### References:
1. Anilist API documentation page: https://docs.anilist.co/
2. Anilist Reference page: https://docs.anilist.co/reference/ 
3. Project using Anilist API/GraphQL: https://medium.com/@jonathan.roman1213/getting-data-from-anilist-co-for-analysis-part-1-building-a-query-using-graphiql-10b7d6d2e350 
4. Anilist API sandbox: https://studio.apollographql.com/sandbox/explorer ( **Particularly helpful if you want to change the querie in these files to fetch different information.** ) 
5. GraphiQL: https://anilist.co/graphiql  
