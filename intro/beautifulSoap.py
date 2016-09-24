from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.aiub.edu")
myBeautifulSoapObject = BeautifulSoup(html.read())
print()
print(myBeautifulSoapObject.h1)
print()
print(myBeautifulSoapObject.html.body.h1)
print()
print(myBeautifulSoapObject.html.h1)
print()
print(myBeautifulSoapObject.html.head.title)
print()
# print(myBeautifulSoapObject.html.head)
# print()
print(myBeautifulSoapObject.html.head.h1) # none
