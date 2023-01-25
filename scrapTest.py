from urllib.request import urlopen

url = input()

response = urlopen(url)
responseHtml = response.read()
responseHtmlDecode = responseHtml.decode('utf-8')
responseHtmlList = responseHtmlDecode.split('"')