import urllib.request # 웹스크래핑을 위함
import re # 정규표현을 위함

# url에서 html 추출하기 위함
url = 'http://www.naver.com'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8') #안해줄 시 한글이 깨질수도 있음

# 정규 표현을 위함
r = re.compile('<span class="news">.*</span>')
m = r.search(html)
s = m.group(0)
print(s)

# 태그 제거 후 값만 추출하기 위함
s = re.sub('<.*?>','',s)
print(s)