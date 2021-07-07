import requests
from bs4 import BeautifulSoup
url = "https://www.manoramamax.com/"

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)	

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

title = soup.title
#print(title)

paras = soup.find_all('p')
#print(paras)

anchors = soup.find_all('a')
#for i in anchors:
#    print(i.get('href'))

all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://manoramamax.com" +link.get('href')
        all_links.add(link)
        print(linkText)