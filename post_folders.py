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
  "id": app.order_id,
  "name": f"{app.name} (Order ID: {str(app.order_id)}) Test15",
  "parent": {
    "id": "202361405223"
  },
  "shared_link": {
    "vanity_name": str(app.order_id),
    "access": "open",
    "permissions": {
      "can_download": True
    }
  }
}

res = requests.post(URL, headers=headers, json=body)

result = res.json()
id = result["id"]

URL = f"https://api.box.com/2.0/folders/{id}?fields=shared_link"

res = requests.put(URL, headers=headers, json=body)
result = res.json(
link = result["shared_link"]
# link_url = link["vanity_url"]
print(link)