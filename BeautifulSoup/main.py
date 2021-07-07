#if you want to scrape a website:
#1. use the api
#2. HTML web scraping using some tool like bs4

#step 0: install all the requirements
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://boston.craigslist.org/search/sof"

#step 1: get the html
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
#print(htmlContent)		# printing the code

#step 2: parse the html
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())	# to print html in tree structure

#step 3: html tree traversal

#commonly used types of object
#print(type(title)) #1. tag
#print(type(title.string)) #2. navigablestring
#print(type(soup)) #3. beautifulsoup
#4. comment
#markup = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(soup2.p)
#print(soup2.p.string)
#print(type(soup2.p.string))

#get the title of the html page
#title = soup.title
#print(title)
#get all the paragraphs from the page
#paras = soup.find_all('p')
#print(paras)
#for i in paras:
#    print(i)

#get first element in the html page
#print(soup.find('p'))

#get classes of any element in the html page
#print(soup.find('p')['class'])

#get all the links on the page
#for i in anchors:
#    print(i.get('href'))

#get all the anchor tags from the page
#anchors = soup.find_all('a')
#for tag in anchors:
 #   print(tag.get('href'))
#print(anchors)
#all_links = set()
#get all the links on the page:
#for i in anchors:
 #   if(i.get('href') != '#'):
  #      link = "http://ceknpy.ac.in/" +i.get('href')
   #     all_links.add(i)
    #    print(link)

#find all the elements with class lead
#print(soup.find_all("p", class_="lead"))
#print(soup.find_all(class_="code-toolbar"))

#get the text from the tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
#navbarSupportedContent = soup.find(id='navbarSupportedContent')
#for elem in navbarSupportedContent.contents:
    #print(elem)

#for item in navbarSupportedContent.strings:
 #   print(item) 

#for item in navbarSupportedContent.stripped_strings:
 #   print(item) 

#print(navbarSupportedContent.parent)
#for item in navbarSupportedContent.parents:
#    print(item)
#    print(item.name)


#print(navbarSupportedContent.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

#elem = soup.select('#loginModal')
#print(elem)

#elem = soup.select('.modal-footer')   # . means class
#print(elem)

jobs = soup.find_all('p',{'class':'result-info'})


for job in jobs:
    title = job.find('a',{'class':'result-title'}).text
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date = job.find('time',{'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nLink:', link, '\n---')