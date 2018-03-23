import re
import urllib.request
import time
import urllib.error
from bs4 import BeautifulSoup

headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

listurl = []

def use_proxy(proxy_addr,url):
    try:
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
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
        print("exception"+str(e))
        time.sleep(1)

def getlisturl(key,pagestart,pageend,proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote("&page")

        for page in range(pagestart,pageend+1):
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)

            data1 = use_proxy(proxy,url)
            # soup = BeautifulSoup(data1,"lxml")
            # print(soup.prettify(()))
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            # listurlpat = 'href="(http://.*?)"'
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

def getcontent(listurl,proxy):
    i= 0
    #设置本地html中的开始编码
    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://
    www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>微信文章页面</title>
<head/>
<body>'''
    fh = open("D:/zxy/GitHub/PythonCrawlerBookCode/Chapter6/1.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()

    fh = open("D:/zxy/GitHub/PythonCrawlerBookCode/Chapter6/1.html","ab")
    for i in range(0, len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url = listurl[i][j]
                url = url.replace("amp;","")
                data = use_proxy(proxy,url)

                titlepat = '<title>(.*?)</title>'
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat,re.S).findall(data)

                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"

                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]

                dataall = "<p>标题为："+thistitle+"</p><p>内容为："+thiscontent+"</p><br>"
                fh.write(dataall.encode('utf-8'))
                print(str(i)+"  "+str(j))

            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)

                time.sleep(10)
            except Exception as e:
                print("exception"+str(e))
                time.sleep(1)
    fh.close()

    html2 = '''</body>
</html>'''

    fh = open("D:/zxy/GitHub/PythonCrawlerBookCode/Chapter6/1.html","ab")
    fh.write(html2.encode('utf-8'))
    fh.close()

key="睡觉"

proxy = "122.114.31.177:808"
proxy2 =""

pagestart=1
pageend=2
listurl=getlisturl(key,pagestart,pageend,None)
getcontent(listurl,proxy)


