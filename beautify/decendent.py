from urllib.request import urlopen
from bs4 import BeautifulSoup

# HTTP error handling
# also tag error handling is not done

# html = urlopen("http://www.pythonscraping.com/.html")
# bsObj = BeautifulSoup(html, "lxml")
#
# # finding children of HTML DOM
# for obj in bsObj.find("table", {"id":"giftList"}).children:
#     print(obj)
#
# # collect data with table row
# for obj in bsObj.find("table", {"id":"giftList"}).siblings:
#     print(obj)
#
# # Dealing with parents
# # remember there is always only one parent
# print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_siblings.get_text())
#
