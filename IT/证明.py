import os
import re
import copy
import math


os.chdir('C:\\Users\\Administrator\\Desktop')

#得到文件的内容
with open('原始数据.xml','rb') as file:
    info = copy.copy(file.read())
info = info.decode('utf8')

#得到各省市的坐标
pro = re.compile(r'<provinces name="(.+?)">').findall(info) 
site = []
for i in range(len(pro)):
    a = re.compile(r'<provinces name="%s">([\s\S]+?)</provinces>' % pro[i]).search(info).group(1)
    b = re.compile(r'<city name="(.+?)" longitude="(.+?)" latitude="(.+?)"/>').findall(a)
    c = {}
    for l in range(len(b)):
        c[b[l][0]] = ((float(b[l][1]),float(b[l][2])))
    site.append(c)

##得到每个省任意点到该省城市的最远距离
##因为如果一个点到中国最近的城市大于上述的最远距离，那必定在国外
print('下表为各个省任意点到本省最近城市的最远距离(数据有序,按照pro表顺序)：')
print('pro表为：')
print(pro)
pro_distance = []
for a in range(len(pro)):
    b = site[a]
    c = list(b.keys())
    d = []
    for e in c:
        for f in c:
            d.append(math.sqrt((b[e][0]-b[f][0])**2 +(b[e][1]-b[f][1])**2))
    pro_distance.append(max(d)/2)
print(pro_distance)

##可能有数据错误的省份为:
unnormal = []
for a in pro_distance:
    if a > 10:
        unnormal.append(a)
print('下面城市可能数据有误:')
for b in unnormal:
    print(pro[pro_distance.index(b)])

print('详细查看五个省份数据异常地方，发现山西，辽宁，新疆确实各有一处地方数据错误')
print('而内蒙古和山东数据较大时因为他们的面积较大！')
print('同样的方法，在数据得到改正后，内蒙古的值确实是该最远距离,为12.39339....故以12.4为准')
