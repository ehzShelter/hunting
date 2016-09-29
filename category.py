from urllib.request import urlopen
from bs4 import BeautifulSoup

urlRef = urlopen("http://www.bdjobs.com")

# bsObj.findAll(tagName, tagAttributes) in order to get a list of all of the tags on the page

# findAll(tag, attribute, recursive, text, limit, keyword)
# by default findAll works recursively set to boolean True
# but first two argument is widely used


bsObj = BeautifulSoup(urlRef, "lxml")


hhhh = bsObj.find("div", {"class":"jobCategory"})

# print(type(hhhh))
print(hhhh.text)
