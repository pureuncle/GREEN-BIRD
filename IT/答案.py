import os
import copy
import re
import math

#修改路径
os.chdir('C:\\Users\\Administrator\\Desktop')

#得到原始文件内容
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

##修改错误数据
site[28]['庄河'] = (122.97,39.7)
site[14]['塔什库尔干'] = (75.22,36.50)
site[11]['万荣'] = (110.83,35.30)

##计算过程
while 1:
    a = input('请输入坐标(经度,纬度)(q!退出)：')
    if a == 'q!':
        break
    else:
        try:
            b = re.compile(r'(.+?),(.+)').findall(a)
            if b is None:
                print('请输入正确的坐标格式！')
                continue
            else:
                c = float(b[0][0])
                d = float(b[0][1])
                try:
                    if int(c) in range(-180,180) and int(d) in range(-180,180):
                        local = (round(c,2),round(d,2))
                        distance = {}
                        for a in range(len(site)):
                            detail = {}
                            for b in site[a]:
                                detail[b] = math.sqrt((local[0] - site[a][b][0])**2 + (local[1] - site[a][b][1])**2)
                            for c in detail:
                                if detail[c] == min(detail.values()):
                                    distance[c] = min(detail.values())
                                    break
                        for a in distance:
                            if distance[a] == min(distance.values()):
                                result = a
                                break
                        if distance[a] < 12.4:
                            for b in range(len(site)):
                                if result in site[b]:
                                    result = '%s-%s' % (pro[b],result)
                                    break
                        else:
                            result = '国外'
                        print(result)
                        continue                        
                    else:
                        print('请输入正确的坐标格式！')
                        continue
                except:
                    print('请输入正确的坐标格式！')
                    continue
        except:
            print('请输入正确的坐标格式！')
            continue

