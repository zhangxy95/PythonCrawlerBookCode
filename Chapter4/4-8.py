import urllib.request
import urllib.error

try:
    urllib.request.urlopen('http://www.1231213.com')
# except urllib.request.HTTPError as e:
#     print(e.code)
#     print(e.reason)
except urllib.request.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)