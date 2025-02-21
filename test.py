import requests

base = "http://127.0.0.1:5000/"
respond = requests.put(base + "vid", {'name':'gg', "likes":"876"})
print(respond.json())