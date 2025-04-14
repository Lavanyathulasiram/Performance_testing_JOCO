API_URL = "https://qa.jocointl.com/search"
WSS_URL = "wss://qa.jocointl.com/searchws"
EXCEL_FILE = "D:\\JOCO_API\\API performace\\Reponsetime.xlsx"

JWT_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJtb2JpbGUiOiI5NTM1MTA0NjM5IiwidXNlcmlkIjoibWFoZW5kcmFuQGdtYWlsLmNvbSIsInN1YiI6IjE2IiwiaWF0IjoxNzQ0NjEwMjc0LCJleHAiOjE3NDUyMTUwNzR9.evV3XAGW467ipkX60WvgXjgVmQMzS_a6g09WVAAGLixbzY19BkyuTY0R3ia1T7HF7N22A246CRqGA4ImWVU3tg"
X_AUTH_TOKEN = "37ba3b01-d8af-43d9-b412-714ef8aa6c5f"

rest_headers = {
    "x-auth-token": X_AUTH_TOKEN,
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"jwtAuthToken={JWT_TOKEN}; TIMEZONE_COOKIE=Asia/Kolkata; accountId=5; roleId=12; baseCurrency=USD;"
}

ws_headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"jwtAuthToken={JWT_TOKEN}; TIMEZONE_COOKIE=Asia/Kolkata; accountId=5; userId=24"
}
