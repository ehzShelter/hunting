from urllib.request import urlopen
from bs4 import BeautifulSoup

gotoLink = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(gotoLink, "lxml")

print(soup.div.h1.get_text())
print(soup.div.h1)
