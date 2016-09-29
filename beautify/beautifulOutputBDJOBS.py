from urllib.request import urlopen
from bs4 import BeautifulSoup

urlRef = urlopen("http://www.bdjobs.com")

# bsObj.findAll(tagName, tagAttributes) in order to get a list of all of the tags on the page

# findAll(tag, attribute, recursive, text, limit, keyword)
# by default findAll works recursively set to boolean True
# but first two argument is widely used


# bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"red"})
bsObj = BeautifulSoup(urlRef, "lxml")

# hotJobs =  bsObj.findAll("div", {"class":"all-jobs"})
# body =  bsObj.body
# print(body)

hhhh = bsObj.find_all("div", class_="hotJobs")

# print(type(hhhh))
print(hhhh)

# all CSS class selector specified as green
# bsObj = BeautifulSoup(urlRef, "lxml").findAll("", {"class":"green"})


# you can use tags as an array to get data back
# bsObj = BeautifulSoup(urlRef, "lxml").findAll({"h1", "h2", "h3", "h4", "h5", "h6"})

# find green first then red
# bsObj = BeautifulSoup(urlRef, "lxml").findAll("span", {"class":"green", "class":"red"})



