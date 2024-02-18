import requests

headers = {"Authorization": "Token 57e3c4dcf70d06a50a3e696737060f4518cf514f"}
base = "http://localhost:8000"

url = base + "/wallets/"

r = requests.get(url, headers=headers)
print("GET all wallets result:")
print(r.text)

url = base + "/transactions/"

r = requests.get(url, headers=headers)
print("GET all transactions result:")
print(r.text)
