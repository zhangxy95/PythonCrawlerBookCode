import re
import urllib.request

def getcontent(url,page):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode("utf-8")


    user_pattern = '<h2>(.*?)</h2>'

    #content_pattern = '<div class="content"><span>(.*?)</span></div>'
    content_pattern = '<span>(.*?)</span>'

    userlist = re.compile(user_pattern,re.S).findall(data)
    contentlist = re.compile(content_pattern,re.S).findall(data)

    index1 = 1

    for content in contentlist:
        content = content.replace("\n"," ")
        name = "content"+str(index1)
        exec(name+'=content')
        index1+=1

    index2 = 1
    for user in userlist:
        name = "content"+str(index2)
        print("用户"+str(page)+str(index2)+":"+user)
        print("内容：")
        exec ("print("+name+")")
        print("\n")
        index2+=1

for i  in range(1,3):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url,i)