import urllib.request

url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")

# filename = urllib.request.urlretrieve(url,filename='F:/Python/PyCharmProjects/PySpiderBook/c4/testcsdn.html')

# 使用bulid_opener修改报头
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

fhandle = open('F:/Python/PyCharmProjects/PySpiderBook/c4/csdn1.html','wb')
fhandle.write(data)
fhandle.close()

# 使用add_header()添加报头

req = urllib.request.Request(url)
req.add_header("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
data1 = urllib.request.urlopen(req).read()
print(data1)