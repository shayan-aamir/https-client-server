import requests

requests_to_send = [
    # 2xx Success
    ("http://localhost:8080/", "GET"),
    ("http://localhost:8080/login", "POST", {"username": "Shayan", "message": "Hello Server!"}),

    # 3xx Redirection
    ("http://localhost:8080/redirect301", "GET"),
    ("http://localhost:8080/redirect302", "GET"),

    # 4xx Client Errors
    ("http://localhost:8080/badrequest", "GET"),
    ("http://localhost:8080/unauthorized", "GET"),
    ("http://localhost:8080/forbidden", "GET"),
    ("http://localhost:8080/notfound", "GET"),

    # 5xx Server Error
    ("http://localhost:8080/servererror", "GET")
]

print("\n=== HTTP STATUS DEMO ===\n")

for item in requests_to_send:
    url = item[0]
    method = item[1]
    data = item[2] if len(item) > 2 else None

    try:
        if method == "GET":
            resp = requests.get(url, allow_redirects=False)  # show 3xx codes without auto-follow
            print(f"[GET] {url} → Status Code: {resp.status_code}")

        elif method == "POST":
            resp = requests.post(url, data=data)
            print(f"[POST] {url} → Status Code: {resp.status_code} | Response: {resp.json()}")

    except Exception as e:
        print(f"[ERROR] {url} → {e}")

print("\n=== DEMO COMPLETE ===\n")

print("""
HTTP STATUS CODES DEMONSTRATED:

200 OK       → Successful request / normal page
301 Moved    → Permanent redirect
302 Found    → Temporary redirect
400 Bad Req  → Client sent invalid request
401 Unauthorized → Auth required
403 Forbidden → Access denied
404 Not Found → Resource missing
500 Internal → Server error
""")

