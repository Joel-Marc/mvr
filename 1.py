import requests
from bs4 import BeautifulSoup
import re
from subprocess import check_output


def popt(inp):
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
    # print(lf)

    te = re.split('\n|�', soup1.get_text())
#te = [x for x in te if x != '�' and x != '']
    # print(te)
    for i in range(0, 5, 2):
        try:
            print("")
            print(te[i], te[i + 1], lf[int(i/2)])
            print("")
        except LookupError:
            print("")


cmd = ['ls', '/mnt/c/Users/joelm/Downloads/ENTERTAINMENT/MOVIES/test']
x = check_output(r'dir "C:\Users\joelm\Downloads\ENTERTAINMENT\MOVIES\test" /B ', shell=True).decode()
y = x.split('\n')
y = [x for x in y if x != '']
# print(x)
print(y)
for i in y:
    popt(i)
