import re

namepat = "<em>(.*?[\u4e00-\u9fa5])</em>"
string ="<em>华为 畅享6 金色 移动联通电信4G手机 双卡双待</em>"
result = re.compile(namepat).findall(string)
print(result)