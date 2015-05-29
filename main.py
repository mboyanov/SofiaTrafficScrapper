import requests
import BeautifulSoup
html_doc = requests.get("http://schedules.sofiatraffic.bg")
#print html_doc.text.encode('ISO-8859-1')
#print html_doc.encoding
soup = BeautifulSoup.BeautifulSoup(html_doc.text.encode('ISO-8859-1'))
transports=[]
for link in soup.findAll('a'):
    if 'tramway' in link.get('href') or 'autobus' in link.get('href') or 'trolleybus' in link.get('href'):
        transports.append(link.get('href'))

import pprint
pprint.pprint(transports)