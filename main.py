import requests
import BeautifulSoup
import collections
html_doc = requests.get("http://schedules.sofiatraffic.bg")
soup = BeautifulSoup.BeautifulSoup(html_doc.text.encode('ISO-8859-1'))
transports=[]
for link in soup.findAll('a'):
    if 'tramway' in link.get('href') or 'autobus' in link.get('href') or 'trolleybus' in link.get('href'):
        transports.append(link.get('href'))

import pprint
pprint.pprint(transports)

karta = collections.defaultdict(lambda: [])
for transport in transports:
	url  = "http://schedules.sofiatraffic.bg/"+transport
	print url
	html_doc = requests.get(url)
	soup = BeautifulSoup.BeautifulSoup(html_doc.text.encode('ISO-8859-1'))
	routes = soup.findAll('ul', { "class" : "schedule_direction_signs" })[:2]

	for route in routes:
		last_stop = None
		stops = route.findAll('li')
		for stop in stops:
			current_stop = stop['class']
			current_stop = current_stop[current_stop.find("stop_")+5:]
			if last_stop:
				karta[last_stop].append(current_stop)
			last_stop = current_stop
