import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
       
        if self.path == '/':
            greeting = os.environ.get('GREETING', 'Hello, World!')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(greeting.encode('utf-8'))
            
      
        elif self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
            
       
        elif self.path == '/notes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            notes = ["купить молоко", "сделать домашку"]
            self.wfile.write(json.dumps(notes, ensure_ascii=False).encode('utf-8'))
            
        
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
  
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f"Server is running on port {port}...")
    server.serve_forever()
