import requests
from bs4 import BeautifulSoup
import re
from subprocess import check_output
from flask import Flask, render_template
app = Flask(__name__)


finlist = []


def popt(inp):
    global finlist
    intdict = {}
    intdict['title'] = inp
    URL = "https://www.google.com/search?q="+inp
    # print(URL)
# URL = "https://www.google.com/search?q=tenet+2020"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    # print(soup)
    table = soup.find_all("div", "Ey4n2", limit=1)
# Ey4n2 ; BNeawe s3v9rd AP7Wnd ; BNeawe vvjwJb AP7Wnd ; kCrY
    x = ''
    for i in table:
        x = x+str(i)

    soup1 = BeautifulSoup(x, 'html5lib')

    l = []
    for links in soup1.find_all('a'):
        l.append(links.get('href'))

    lf = []
    temp = []
    for i in l:
        i = i[7:]
        temp = i.split('&')
        i = '<a href=\"' + temp[0] + '\">Click Here</a>'
        lf.append(i)
    # print(lf)

    te = re.split('\n|�', soup1.get_text())
# te = [x for x in te if x != '�' and x != '']
    # print(te)
    sp = []
    for i in range(0, 3, 2):
        try:
            # print("")
            # print(te[i], te[i + 1], lf[int(i/2)])
            intdict[te[i+1]] = te[i]
            intdict[str('link'+str(int(i/2)))] = lf[int(i/2)]
            print(intdict[te[i+1]], te[i+1])
            if '/' in intdict[te[i+1]]:
                sp.append(float(intdict[te[i+1]].split('/')[0])*10)
                print(float(sp[0]) * 10)
            elif '%' in intdict[te[i+1]]:
                sp.append(float(intdict[te[i+1]].split('%')[0]))
                print(float(sp[0]))

            # print("")
        except LookupError:
            print("")
        try:
            intdict['score'] = sum(sp)/len(sp)
        except:
            intdict['score'] = 0
    # print(intdict)
    intdict['...'] = ' '
    finlist.append(intdict)


x = check_output(r'ls "/media/jmarc/New Volume/ENTERTAINMENT/MOVIES"', shell=True).decode()
y = x.split('\n')
y = [x for x in y if x != '']
print(x)
print(y)
for i in y:
    popt(i)


finlist = sorted(finlist, key=lambda x: x['score'], reverse=True)

print(finlist)

# for k in finlist:
#     for za, zu in k.items():
#         print(za, zu)


@app.route('/')
def home():
    return render_template('index.html', posts=finlist)


if __name__ == '__main__':
    app.run(debug=True)
