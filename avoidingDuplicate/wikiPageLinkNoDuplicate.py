from urllib.request import urlopen
from bs4 import BeautifulSoup
# regular expression
import re

# memoization
# set container of Python
pages = set()
# remember the explored link

def getHttpLinkOnly(pageURL):
    # making pages variable lexical
    global pages
    html = urlopen("http://en.wikipedia.com"+pageURL)
    bsObj = BeautifulSoup(html)
    # recall
    # findAll takes tag as first parameter and attribute second parameter
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        # if link you can traverse
        if 'href' in link.attrs:
            # If link in stored already in pages variable don't crawl
            if link.attrs['href'] not in pages:
                # we have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getHttpLinkOnly(newPage)



getHttpLinkOnly("") # This will redirect to root pages


# Initially getHttpLinkOnly("") is called with an empty URL. This is translated as “the front page
# of Wikipedia” as soon as the empty URL is prepended with http://en.wikipe
# dia.org inside the function. Then, each link on the first page is iterated through and
# a check is made to see if it is in the global set of pages
