from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')
print('URL Opened :', req)

xml = BeautifulSoup(req, 'lxml.parser')

#for item in xml.findAll('link'):
#    print(item)

