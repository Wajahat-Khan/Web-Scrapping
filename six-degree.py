from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
try:
    html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon');
    bs=BeautifulSoup(html, 'html.parser')
except HTTPError as e:
    print(e)
for links in bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(\/wiki\/)((?!:).)*$')):
    if 'href' in links.attrs:
        print(links['href'])
