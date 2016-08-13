from bs4 import BeautifulSoup
import requests
import time
import csv

count = 0     # pages to traverse; max = 100
term = "dentist"
loc= 10010  #zipcode

#storing the results here
collection = [] #first req
results = [["YELP URL", "Business Name", "Address", "Telephone", "URL", "AVERAGE RATING", "REVIEWS"]] #final results
currentCount = 0

#extract the results from the page
def resultsExtract(soup):
	for link in soup.find_all('a'):
		try:
			#if it contains the biz-name class grab it's url
			if((link.get('class')[0].find('biz-name') != -1) & (link.get('href').find('/biz') != -1)):
				collection.append("http://www.yelp.com" + link.get('href'))
		except Exception, e:
			4+4
#end resultsExtract

#info from the page
def pageParse(link):
	r = requests.get(link)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")

	#parse telephone
	tel = ''
	spans = soup.find_all('span')
	for span in spans:
		try:
			if(span.get('class')[0] == 'biz-phone'):
				tel = span.text.strip()
				break
		except Exception, e:
			4+4
	#end parse telephone

	#parse biz website
	web = ''
	webs = soup.find_all('a')
	for a in webs:
		try:
			if(a.text.find('.com') != -1):
				web = a.text.strip()
				break
		except Exception, e:
			4+4
	#end website

	#parse rating
	rating = ''
	items = soup.find_all('i')
	for item in items:
		try:
			if(item.get('title').find('star') != -1):
				rating = item.get('title')
		except Exception, e:
			4+4
	#end rating

	#parse telephone
	reviewCount = ''
	spans = soup.find_all('span')
	for span in spans:
		try:
			if(span.get('itemprop') == 'reviewCount'):
				reviewCount = span.text
				break
		except Exception, e:
			4+4
	#end parse telephone

	result = [
		link,
		soup.find('h1').text.strip(),
		soup.find('address').text.strip(),
		tel,
		web,
		rating,
		reviewCount
	]

	results.append(result)



#grab multiple pages of results
while(currentCount <= count):
	url = "http://www.yelp.com/search?find_desc="+term+"&find_loc="+ str(loc) +"&start="+ str(currentCount*10)
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	print('Getting page: '+ str(currentCount))
	resultsExtract(soup)
	time.sleep(1)
	currentCount+=1

# print(collection)

#Now to work on the entire collection
while(len(collection) !=0 ):
	link = collection.pop()
	print('Getting data on '+ link)
	pageParse(link)
	time.sleep(1)

# print(results)

#output csv
print('DONE! Check out output.csv for your results.')
with open("output.csv", "wb") as f:
  writer = csv.writer(f)
  writer.writerows(results)



