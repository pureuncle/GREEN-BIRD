import urllib.request
import re
import matplotlib.pyplot as plt

def r(a):
    b = list(a)
    b.reverse()
    return ''.join(b)

def f(name,time):
    box = []
    for i in time:
        url = 'https://box.maoyan.com/promovie/api/box/second.json?beginDate=%s' % (i)
        url = urllib.request.Request(url)
        url.add_header = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
        data = urllib.request.urlopen(url)
        html = data.read().decode('utf8')
        html = r(html)
        info = re.compile(r'"%s":"emaNeivom"(.+?):"ofnIwohs"{' % r(name)).search(html).group()
        info = r(info)
        box_office = re.compile(r'"boxInfo":"(.+?)",').search(info).group(1)
        box_office = float(box_office)
        box.append(box_office)


    date = []
    for l in time:
        date.append(str(l)[-4:])

    plt.plot(time,box)
    plt.xlabel('date')
    plt.ylabel('box office')
    plt.xticks(time,date)

    plt.show()
