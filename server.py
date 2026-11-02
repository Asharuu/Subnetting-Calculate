import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 5173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"==================================================")
        print(f" Pohon Subnetting Interaktif (Iza's Way) ")
        print(f" Modul 7 - Jaringan Komputer (Kelas C) ")
        print(f" Server berjalan di: {url}")
        print(f" Tekan Ctrl+C untuk menghentikan server.")
        print(f"==================================================")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")
            sys.exit(0)
