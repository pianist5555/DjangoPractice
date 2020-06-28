import urllib.request
import urllib.parse

# 초창기 CGI 방식
# 클라이언트에서 요청되는 주소가 CGI에 대응되는 지를 확인하고 대응 된다면 독립적인 프로세스로 작동
# * 요청이 들어올 떄마다 처리를 위한 프로세스가 생성 -> 서버의 부하가 높아진다. 
# CGI: 요청 -> 웹서버(아파치, nginx 등) -> (웹서버가 직접실행) 프로그램(perl,C/C++ 등)
# WAS: 요청 -> 웹서버 -> 웹 어플리케이션 서버(톰캣, JBoss 등) -> (웹 어플리케이션 서버가 실행) 프로그램
# WSGI: 요청 -> 웹서버 -> WSGI Server(=미들웨어) -> WSGI를 지원하는 웹 어플리케이션 (Django, flask 등)

data = {
    'name': '박선오',
    'email': 'pianist5555@gmail.com',
    'url': 'http://www.google.com'
}

postData = urllib.parse.urlencode(data).encode('UTF-8')
url = urllib.request.Request("http://localhost:8888/cgi-server/cgi-bin/script.py", postData)
resp = urllib.request.urlopen(url).read().decode('UTF-8')

print(resp)