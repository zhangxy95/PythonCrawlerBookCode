import re
import urllib.request
import time
import urllib.error

headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

listurl = []

def use_proxy(proxy_addr,url):
    try:
        proxy = urllib.request.ProxyHandler({'http:proxy_addr'})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        time.sleep(1)

def getlisturl(key,pagestart,pageend,proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote("&page")

        for page in range(pagestart,pageend):
            url = "http://weixin.sogou.com/weixin?tyep=2&query="+keycode+pagecode+str(page)

            data1 = use_proxy(proxy,url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("共获取到"+str(len(listurl))+"页")
        return listurl
    except urllib.request.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print(str(e))
        time.sleep(1)

# to be continued
def getcontent(listurl,proxy):
    pass

