import requests
import time
import json

class Taw:
    def taw():
        #当前时间
        t = time.ctime()

        #当前天气
        w = requests.get("http://www.weather.com.cn/data/cityinfo/101010100.html")
        w.encoding='utf-8'
        r = w.json()

        return t ,r


