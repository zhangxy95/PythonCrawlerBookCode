import urllib.request
import urllib.parse
import http.cookiejar

# url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q'
# postdata = urllib.parse.urlencode({
#     "username":"zxy0425",
#     "password":"zhangxinyan0425"
# }).encode('utf-8')
#
# req = urllib.request.Request(url,postdata)
# req.add_header("User-Agent",
#            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
# data = urllib.request.urlopen(req).read()
# fhandle = open('D:/zxy/GitHub/PythonCrawlerBookCode/Chapter5/1.html','wb')
# fhandle.write(data)
# fhandle.close()
#
# url2 = 'http://bbs.chinaunix.net'
# req2 = urllib.request.Request(url2,postdata)
# req2.add_header("User-Agent",
#            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
# data2 = urllib.request.urlopen(req2).read()
# fhandle = open('D:/zxy/GitHub/PythonCrawlerBookCode/Chapter5/2.html','wb')
# fhandle.write(data2)
# fhandle.close()

url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q'
postdata = urllib.parse.urlencode({
    "username":"zxy0425",
    "password":"zhangxinyan0425"
}).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
# 使用cookiejar
cjar = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 一个全局opener
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()
fhandle = open('D:/zxy/GitHub/PythonCrawlerBookCode/Chapter5/3.html','wb')
fhandle.write(data)
fhandle.close()

url2 = 'http://bbs.chinaunix.net'
# 使用urlopen就会用那个opener
data2 = urllib.request.urlopen(url2).read()
fhandle = open('D:/zxy/GitHub/PythonCrawlerBookCode/Chapter5/4.html','wb')
fhandle.write(data2)
fhandle.close()