#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2
i=0;
desiredurl = raw_input("Enter the url ");
url= "https://www.alexa.com/siteinfo/"+desiredurl
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

for pagetext in  soup.find_all('strong',{'class' : 'metrics-data align-vmiddle'}):
       
		print "**********  GLOBAL RANK FOR",desiredurl,"*********"; 
		print pagetext.text
                break;
