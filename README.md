#Business Scraper
=================
Simple project to scrape website urls and phone numbers of businesses that aren't mobile optimized. I favored yelp's results from their API for the simplicity of defining location. Plus whoever is on there would already have some kind of online presence.  

##TODO
======
-Query Yelp correctly for a telephone number
-Get website url from yellowpages
-check if website is mobile optimized
-Save to csv

##Usage
=======
Make sure to make a file with your yelp developer keys: **yelp.json**. The format for that is as follows, in json of course.
And to also install the reqired packages in your virtualenv with **pip install -r requirements.txt**. 

```json
{
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "token": "YOUR_TOKEN",
    "token_secret": "YOUR_TOKEN_SECRET"
}
```