from requests import get
from json import loads

def getDetails(ipAddress):
    r = get('http://ip-api.com/json/{0}'.format(ipAddress))
    data = loads(r.content)
    return data

ipAddress = input("Enter ip address to track: ")
data = getDetails(ipAddress)
for key, value in data.items():
    print(key, ":", value)
