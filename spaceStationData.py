import urllib3
import urllib.request as urllib2
import json

req = urllib3.request("GET", "http://api.open-notify.org/iss-now.json")

obj = json.loads(req.data)

print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])

def get_latitude():
    latitude = obj['iss_position']['latitude']
    print(latitude)
    return float(latitude)

def get_longitude():
    longitude = obj['iss_position']['longitude']
    print(longitude)
    return float(longitude)

