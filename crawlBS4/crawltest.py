from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup


# url = "https://www.naver.com"
url = "https://m.blog.naver.com/heerok93/221076782232"

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.text
    except AttributeError as e:
        print(e)
        return None
    return title

# title = getTitle(url)
#
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)


a=[[1,2,3,4],[5,6,7,8,9]]
print(len(a[1]))