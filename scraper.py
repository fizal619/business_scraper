import sys 
import io
import json

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

print(results.total + " results for " + term + " in " + place)
print(results.business[0].name + " is the first item on the list.")

# iterate array and extract 





