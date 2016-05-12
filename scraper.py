import sys 
import io
import json
import urllib2

from yelp.client import Client 
from yelp.oauth1_authenticator import Oauth1Authenticator

from time import sleep

term= sys.argv[1] 
place= sys.argv[2].split()
 

# read API keys
with io.open('yelp.json') as cred:
	creds = json.load(cred)
	auth = Oauth1Authenticator(**creds)
	client = Client(auth)


# make request for the search term store in array

params = {
    'term': term,
    'limit': '20',
    'lang': 'en'
}

# YellowPages creds
with io.open('yp.json') as cred:
	yp_creds = json.load(cred)
	
#data = json.load(urllib2.urlopen('http://someurl/path/to/json'))

# iterate array and extract the ones that have a web url in their yellowpages listings. 
for i in range(int(place[0]), int(place[1])): 
	
	results = client.search(str(i), **params)
	print(str(results.total) + " results for " + term + " in " + str(i))
	print('Results have ' + str(len(results.businesses)) + ' items')

	for business in results.businesses:
		print("Getting data for " + business.name)
		term = business.phone
		
		try:
			data = json.load(urllib2.urlopen("http://api2.yp.com/listings/v1/search?format=json&key=" + yp_creds["API_Key"] + "&searchloc=" + str(i) + "&term=" + term + "&phonesearch=true"))
			try:
				if data["searchResult"]["searchListings"]["searchListing"][0]["websiteURL"] != '':
					print(data["searchResult"]["searchListings"]["searchListing"][0]["websiteURL"])
			except TypeError:
				print('No data, TypeError for some reason.')	
		except IndexError, HTTPError:
			print('No data returned.')

		print('')
		sleep(1)



