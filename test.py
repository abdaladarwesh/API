import requests

base = "http://127.0.0.1:5000/"
putReq1 = requests.put(base + "vid/1", {"views":15, "name":"abdallah"})
putReq2 = requests.put(base + "vid/2", {"name":"laila", "views":66})
print(putReq1.json())
print(putReq2.json())
input()
getreq1 = requests.get(base + "vid/1")
getreq2 = requests.get(base + "vid/2")
print(getreq1.json())
print(getreq2.json())
delreq1 = requests.delete(base + "vid/1")
getreq1 = requests.get(base + "vid/1")
getreq2 = requests.get(base + "vid/2")
print(getreq1.json())
print(getreq2.json())


