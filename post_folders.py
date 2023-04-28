import requests, app

with open("access_token.txt", "r") as f:
  ACCESS_TOKEN = f.read().strip()

URL = "https://api.box.com/2.0/folders"
ACCESS_TOKEN = f"Bearer {ACCESS_TOKEN}"

headers = {
  "Authorization": ACCESS_TOKEN,
  "Content-Type": "application/json"
}

body = {
  "name": f"{app.name} (Order ID: {str(app.order_id)})",
  "parent": {
    "id": "202361405223"
  }
}

res = requests.post(URL, headers=headers, json=body)
status = res.status_code
print(status)