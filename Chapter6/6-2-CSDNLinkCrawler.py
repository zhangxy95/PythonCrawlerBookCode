import re
import urllib.request

def getlink(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
    opener = urllib.request.build_opener()
    opener.addheaders=[headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())

    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #print(link)
    # 变成set 去重
    link = list(set(link))
    return link

url = "http://blog.csdn.net"

linklist = getlink(url)

for link in linklist:
    print(link[0])