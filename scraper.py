import sys 
import io
import json
import urllib2

from yelp.client import Client 
from yelp.oauth1_authenticator import Oauth1Authenticator

term= sys.argv[1] 
place= sys.argv[2] 
 

# read API keys
with io.open('yelp.json') as cred:
	creds = json.load(cred)
	auth = Oauth1Authenticator(**creds)
	client = Client(auth)


# make request for the search term store in array

params = {
    'term': term,
    'lang': 'en'
}

results = client.search(place, **params)

print(str(results.total) + " results for " + term + " in " + place)


# YellowPages creds
with io.open('yp.json') as cred:
	yp_creds = json.load(cred)
	
#data = json.load(urllib2.urlopen('http://someurl/path/to/json'))

# iterate array and extract the ones that have a web url in their yellowpages listings. 
for i in range(10):
	print("Getting data for " + results.businesses[i].name)
	term = results.businesses[i].phone

	data = json.load(urllib2.urlopen("http://api2.yp.com/listings/v1/search?format=json&key=" + yp_creds["API_Key"] + "&searchloc=" + results.businesses[i].location.postal_code + "&term=" + term + "&phonesearch=true"))
	if data["searchResult"]["searchListings"]["searchListing"][0]["websiteURL"] != '':
		print(data["searchResult"]["searchListings"]["searchListing"][0]["websiteURL"])
	else:
		print("No website URL available for " + results.businesses[i].name)
	print('')



