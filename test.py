import requests

base = "http://127.0.0.1:5000/"
putReq1 = requests.put(base + "vid/5", {"views":4567, "name":"gg"})
putReq2 = requests.put(base + "vid/6", {"name":"yy", "views":98634})
print(putReq1.json())
print(putReq2.json())
input()
getreq1 = requests.get(base + "vid/5")
getreq2 = requests.get(base + "vid/6")
print(getreq1.json())
print(getreq2.json())
