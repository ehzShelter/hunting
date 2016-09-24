from urllib.request import urlopen
from bs4 import BeautifulSoup

urlRef = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

# bsObj.findAll(tagName, tagAttributes) in order to get a list of all of the tags on the page
bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"green"})

for name in bsObj:
    # .get_text() strips all tags from the document you are working with and returns a string containing the text only
    print(name.get_text())

