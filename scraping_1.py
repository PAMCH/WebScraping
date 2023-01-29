import urllib.request

url = 'http://www.naver.com'

res = urllib.request.urlopen(url)

html = res.read().decode('utf-8')

print(html)