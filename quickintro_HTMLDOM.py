from bs4 import BeautifulSoup
import urllib

r = urllib.request.urlopen('http://www.aiub.edu').read()

# Beautiful Soup is essentially a set of wrapper functions that make it simple to select common HTML elements

soup = BeautifulSoup(r, "lxml")
print(type(soup.prettify()))

hell = soup.prettify()
print(hell)

# Make sure IPython installed in your System PATH
from IPython.display import Image
Image('http://www.cs.toronto.edu/~shiva/cscb07/img/dom/treeStructure.png')

