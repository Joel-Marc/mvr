import requests
from bs4 import BeautifulSoup
import re


inp = input("ENTER MOVIE TITLE : ")
inp = inp.replace(" ", "+")
URL = "https://www.google.com/search?q="+inp
print(URL)
#URL = "https://www.google.com/search?q=tenet+2020"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')


table = soup.find_all("div", "Ap5OSd", limit=1)

x = ''
for i in table:
    x = x+str(i)

soup1 = BeautifulSoup(x, 'html5lib')

l = []
for links in soup1.find_all('a'):
    l.append(links.get('href'))

lf = []
for i in l:
    i = i[7:]
    lf.append(i)
print(lf)

te = re.split('\n|�', soup1.get_text())
#te = [x for x in te if x != '�' and x != '']
print(te)
for i in range(0, 5, 2):
    print(te[i], te[i + 1])
# print(table)
# for i in table:
#     print(i)
