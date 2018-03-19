import re
import urllib.request
import urllib.error

def crawJD(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)

    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]

    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)

    # 添加手机名称
    namepat  = "<em>(.*?[\u4e00-\u9fa5])</em>"
    namelist = re.compile(namepat).findall(result1)
    print(namelist)

    index = 1
    for imageurl in imagelist:
        imagename = "D:/zxy/JDpic/"+str(page)+str(index)+".jpg"
        imageurl = "http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                index+=1
            if hasattr(e,"reason"):
                index+=1
        index+=1


for i in range(1,5):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    crawJD(url,i)
    print(i)
