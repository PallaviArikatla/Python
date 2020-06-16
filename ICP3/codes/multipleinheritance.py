import requests
from bs4 import BeautifulSoup

url=requests.get("https://en.wikipedia.org/wiki/Deep_learning").text
soup=BeautifulSoup(url,"html.parser")

title=soup.find('title')
print(title.string)

aTags=soup.find_all('a')

file=open('links.txt','a+',encoding='utf-8')

for tag in aTags:
    if tag.get('href'):
        href=tag.get('href')
        file.write(str(href)+'\n')
        print(href)