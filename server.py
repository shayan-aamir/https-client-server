from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"[GET] Path requested: {self.path}")

        # 3xx Redirection examples
        if self.path == "/redirect301":
            self.send_response(301)
            self.send_header("Location", "/")
            self.end_headers()
            return

        if self.path == "/redirect302":
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()
            return

        # 4xx Client errors
        if self.path == "/badrequest":
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"400 Bad Request")
            return
        if self.path == "/unauthorized":
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"401 Unauthorized")
            return
        if self.path == "/forbidden":
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"403 Forbidden")
            return
        if self.path == "/notfound":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        # 5xx Server error
        if self.path == "/servererror":
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 Internal Server Error")
            return

        # 200 OK normal pages
        if self.path == "/":
            self.path = "/static/login.html"
        elif self.path == "/dashboard":
            self.path = "/static/dashboard.html"

        try:
            if self.path.startswith("/static/"):
                file_path = "." + self.path
                if os.path.exists(file_path):
                    with open(file_path, "rb") as file:
                        self.send_response(200)
                        content_type = "text/html" if self.path.endswith(".html") else "text/plain"
                        self.send_header("Content-type", content_type)
                        self.end_headers()
                        self.wfile.write(file.read())
                        return
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"404 Not Found")
                    return

            # fallback 404
            self.send_response(404)
            self.end_headers()

        except Exception as e:
            print("ERROR:", e)
            self.send_response(500)
            self.end_headers()

    def do_POST(self):
        print(f"[POST] Path requested: {self.path}")

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = urllib.parse.parse_qs(body)
        print("📌 Data received from client:", data)

        # login example
        if self.path == "/login":
            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]
            print(f"User tried to login with: {username} / {password}")

            if username == "admin" and password == "123":
                response = {"success": True, "redirect": "/dashboard"}
            else:
                response = {"success": False, "message": "Invalid credentials"}
        else:
            response = {"status": "received", "data": data}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def run():
    print("Server running on http://localhost:8080")
    server = HTTPServer(("localhost", 8080), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()

