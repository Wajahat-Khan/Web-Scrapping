from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for sibling in bs.find('table', {'id':'giftList'}).tr.descendants:
    print(sibling)


# .parents, .parents, .next_sibling(s), .previous_sibling(s) are also there