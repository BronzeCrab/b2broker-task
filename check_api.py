import requests

headers = {"Authorization": "Token 1243af14e14e0772d3d987c3f9cffbd6802002ab"}
base = "http://localhost:8000"

url = base + "/wallets/"

r = requests.get(url, headers=headers)
print("GET all wallets result:")
print(r.text)

url = base + "/transactions/"

r = requests.get(url, headers=headers)
print("GET all transactions result:")
print(r.text)
