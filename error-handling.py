from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(title):
    try:
        html=urlopen(title)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print('Server not found')
        return None
    try:
        bs=BeautifulSoup(html.read(),'html.parser')
        title=bs.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
    print('Title not found')
else:
    print(title)