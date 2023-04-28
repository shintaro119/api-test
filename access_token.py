import requests, client

URL = "https://api.box.com/oauth2/token"
CODE = "6RdqhaaNJ790bN1KhOdKW9k1bWUrr6um"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}

data = {
  "client_id": client.CLIENT_ID,
  "client_secret": client.CLIENT_SECRET,
  "code": CODE,
  "grant_type": "authorization_code"
}

res = requests.post(URL, headers=headers, data=data)
result = res.json()
ACCESS_TOKEN = result["access_token"]
REFRESH_TOKEN = result["refresh_token"]

with open("access_token.txt", "w") as f:
  f.write(ACCESS_TOKEN)

with open("refresh_token.txt", "w") as f:
  f.write(REFRESH_TOKEN)