import requests

base = "http://127.0.0.1:5000/"
response = requests.put(base + "video/1", {"name":"8", "likes":"67", "views":15})
print(response.json())