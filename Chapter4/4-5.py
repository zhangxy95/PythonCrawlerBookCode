import urllib.request
import urllib.parse

# GET
# keywd = '张新研'
#
# key = urllib.request.quote(keywd)
# url = 'http://www.baidu.com/s?wd='+key
#
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()
# fhandle = open('F:/GitHub/PythonSpiderBookCode/Chapter4/45get.html','wb')
# fhandle.write(data)
# fhandle.close()

# POST

url = 'http://www.iqianyue.com/mypost'
postdata = urllib.parse.urlencode({
    "name":"zxy",
    "pass":"zxy0425"
}).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")

data = urllib.request.urlopen(req).read()
fhandle = open('F:/GitHub/PythonSpiderBookCode/Chapter4/45post.html','wb')
fhandle.write(data)
fhandle.close()