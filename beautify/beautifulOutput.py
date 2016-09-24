from urllib.request import urlopen
from bs4 import BeautifulSoup

urlRef = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

# bsObj.findAll(tagName, tagAttributes) in order to get a list of all of the tags on the page

# findAll(tag, attribute, recursive, text, limit, keyword)
# by default findAll works recursively set to boolean True
# but first two argument is widely used


# bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"red"})
bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"green"})

# all CSS class selector specified as green
# bsObj = BeautifulSoup(urlRef, "lxml").findAll("", {"class":"green"})


# you can use tags as an array to get data back
# bsObj = BeautifulSoup(urlRef, "lxml").findAll({"h1", "h2", "h3", "h4", "h5", "h6"})

# find green first then red
# bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"green", "class":"red"})

for name in bsObj:
    # .get_text() strips all tags from the document you are working with and returns a string containing the text only
    print(name.get_text())
    # find the length of every name
    # print(len(name.get_text()))

nameSpecified = BeautifulSoup(urlRef, "lxml").findAll(text="the Sohan")
# Sohan is not there
print(len(nameSpecified))


