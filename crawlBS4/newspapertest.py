from newspaper import Article
import newspaper
from newspaper import fulltext
#크롤링할 url 주소 입력
# url = 'http://v.media.daum.net/v/20170604205121164'
# url = "https://m.blog.naver.com/heerok93/221076782232"
# url = "https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html"
url = "http://sports.news.naver.com/wfootball/schedule/index.nhn"
#===========================================
#언어가 한국어이므로 language='ko'로 설정
a = Article(url, language='ko')
a.download()
a.parse()
#기사 제목 가져오기
print(a.title)
#기사 내용 가져오기(150자)
# print(a.text)
with open('newspp.html','w') as f:
    # text = fulltext(a.html)
    f.write(a.html)

a.build()
with open('newspp_1.html','w') as f:
    # text = fulltext(a.html)
    f.write(a.html)


print(a.publish_date)
print(a.images)
#===========================================
# nb = newspaper.build(url)
#
# for article in nb.category_urls():
#     print(article)
#===========================================