from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body
    except AttributeError as e:
        return None

    return title


# calling getTitle(url) func
theTitle = getTitle(" http://jobs.bdjobs.com/jobsearch.asp")
if theTitle == None:
    print("Title could not found")
else:
    print(theTitle)
