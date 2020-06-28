import urllib.request

#웹 클라이언트로 HTTP 요청을 단 두 줄로 보냈다!
#print(urllib.request.urlopen("http://www.example.com").read().decode('utf-8'))

# from urllib.parse import urlparse # url 분해, 조립 파싱관련 모듈
# result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
# print(result)

from urllib.request import HTTPBasicAuthHandler, build_opener
auth_handler = HTTPBasicAuthHandler() 
auth_handler.add_password(realm='ksh', user='shkim', passwd='shkimadmin',
uri='http://127.0.0.1:8000/auth/')
opener = build_opener(auth_handler)
resp = opener.open('http://127.0.0.1:8000/auth/')
print(resp.read().decode('utf-8'))
