import requests, client

with open("access_token.txt", "r") as f:
  ACCESS_TOKEN = f.read()

with open("refresh_token.txt", "r") as f:
  REFRESH_TOKEN = f.read()

URL = "https://api.box.com/oauth2/token"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}

data = {
  "client_id": client.CLIENT_ID,
  "client_secret": client.CLIENT_SECRET,
  "refresh_token": REFRESH_TOKEN,
  "grant_type": "refresh_token"
}

res = requests.post(URL, headers=headers, data=data)
result = res.json()
ACCESS_TOKEN = result["access_token"]
REFRESH_TOKEN = result["refresh_token"]

with open("access_token.txt", "w") as f:
  f.write(ACCESS_TOKEN)

with open("refresh_token.txt", "w") as f:
  f.write(REFRESH_TOKEN)