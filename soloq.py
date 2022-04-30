import sys
import string
import urllib.request

user = sys.argv[1]
url = 'https://euw.op.gg/summoners/euw/' + user
page = urllib.request.urlopen(url).read().decode()

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

elo = soup.find("div", attrs={"class": "tier-rank"}).get_text()
lp = soup.find("span", attrs={"class": "lp"}).get_text()
win = soup.find("span", attrs={"class": "win-lose"}).get_text()
print(user + " " + elo + " " + lp + " " + win)