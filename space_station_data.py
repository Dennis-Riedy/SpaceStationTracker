"""
Functionality to take in location data of the Internation Space Station.
"""

import json
import urllib3

# TODO: Error handling around connections 
req = urllib3.request("GET", "http://api.open-notify.org/iss-now.json")

obj = json.loads(req.data)

print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])


def get_latitude():
    """Get Latitude for coordinates"""
    latitude = obj['iss_position']['latitude']
    print(latitude)
    return float(latitude)

def get_longitude():
    """Get Longitude coordinates"""
    longitude = obj['iss_position']['longitude']
    print(longitude)
    return float(longitude)
