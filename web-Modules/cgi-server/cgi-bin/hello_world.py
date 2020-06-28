from http.server import HTTPServer, BaseHTTPRequestHandler
# HTTPServer: 웹서버를 만들기 위한 클래스 (IP, Port로 바인딩함), HTTPServer 객체 생성시 핸들러 클래스가 반드시 필요함
# BaseHTTPRequestHandler: 핸들러를 만들기 위한 기반 클래스, HTTP 프로토콜 처리 로직이 들어있다, 이 클래스를 상속받아 자신의 핸들러 클래스를 만듬
# SimpleHTTpRequestHandler: BaseHTTPRequestHandler를 상속받았고 GET과 HEAD 메소드 처리가 가능한 핸들러 클래스 -> python -m http.server 8888 로 간편 실행
# CGIHTTPRequestHandler: SimpleHTTpRequestHandler를 상속받았고 POST 메소드와 CGI 처리가 추가된 핸들러 클래스 -> python -m http.server 8888 --cgi 로 간편 실행

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler) # HTTPServer 객체 생성
    print("Strated WebServer on port 8888...")
    print("Press ^C to quit WebServer.")
    server.serve_forever() # HTTPServer 객체의 serve_forever 메소드 실행