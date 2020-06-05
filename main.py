import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
print("{0:<15}" "{1:>50}".format("Item Name","Behemoth Name"))
def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup
content = getHTMLContent("https://dauntless.gamepedia.com/Reagents")
tables = content.find_all('table')
    
table = content.find('table', {'class': 'wikitable sortable'})
rows = table.find_all('tr')

table = content.find('table', {'class': 'wikitable sortable'})
rows = table.find_all('tr')
# List of all links
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        item_name = cells[1].find('a')
        behemoth_name = cells[3].find('a')
        item_rarity = cells[4].find('a')
        print("{0:<15}" "{1:>50}".format(item_name.get('href').replace("/","").replace("_"," "),behemoth_name.get('href').replace("/","").replace("_"," ").replace("Behemoths#Enraged","Enraged Behemoths").replace("Behemoths#Aether Charged","Aether Charged Behemoths")))