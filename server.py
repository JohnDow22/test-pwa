import http.server
import ssl

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Используем порт 443 (стандартный для HTTPS) или 8443 если без sudo
port = 8443  
server_address = ('0.0.0.0', port)

httpd = http.server.HTTPServer(server_address, Handler)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f'Запуск HTTPS сервера на порту {port}...')
print(f'Откройте https://95.179.233.26:{port}/')
httpd.serve_forever()