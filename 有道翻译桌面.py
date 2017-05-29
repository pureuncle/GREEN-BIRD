import urllib.request
import urllib.parse
import json



while 1:
    content = input("请输出翻译的内容（q!退出）：")
    if content != "q!":
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.sogou.com/sie"
        urll = urllib.request.Request(url)
        urll.add_header = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
        data = {}
        data["type"] = "AUTO"
        data["i"] = content
        data["doctype"] = "json"
        data["xmlVersion"] = "1.8"
        data["Keyfrom"] ="fanyi.web"
        data["ue"] = "UTF-8"
        data["action"]="FY_BY_CLICKBUTTON"
        data["typoResult"] = "true"

        data = urllib.parse.urlencode(data).encode("utf-8")

        response = urllib.request.urlopen(urll,data)
        html = response.read().decode("utf-8")

        target = json.loads(html)
        result = target['translateResult'][0][0]['tgt']
        print("翻译结果为：" + result)
        continue
    else:
        print("结束！")
        break
