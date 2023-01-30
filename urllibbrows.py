import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href', None))