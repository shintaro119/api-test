import requests

URL = "https://api-test-s.myshopify.com/admin/api/2023-04/orders.json"
TOKEN = "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"

headers = {
  "X-Shopify-Access-Token": TOKEN,
  "Content-Type": "application/json"
}

res = requests.get(URL, headers=headers)
# res_s: Shopify API Response
result = res.json()

orders = result["orders"]
order = orders[0]
order_id = order["id"]

customer = order["customer"]
first_name = customer["first_name"]
last_name = customer ["last_name"]
name = first_name + " " + last_name

# https://account.box.com/api/oauth2/authorize?client_id=dylvrpea0nib9ojgmkza0yeau3tsbjfj&redirect_uri=http://localhost:8080/&response_type=code
