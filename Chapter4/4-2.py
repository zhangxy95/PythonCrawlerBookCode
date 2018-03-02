import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
dataline = file.readline()

print(dataline)
print(data)

# fhandle = open("F:/Python/PyCharmProjects/PySpiderBook/c4/baidu.html",'wb')
# fhandle.write(data)
# fhandle.close()

# filename = urllib.request.urlretrieve('http://www.163.com',filename='F:/Python/PyCharmProjects/PySpiderBook/c4/163.html')

urllib.request.urlcleanup()

print(file.info())

# google = urllib.request.urlopen('http://www.google.com')
# print(google.getcode())

print(file.geturl())

sina1 =urllib.request.quote('http://www.sina.com')
print(sina1)

sina2 =urllib.request.unquote("http%3A//www.sina.com")
print(sina2)