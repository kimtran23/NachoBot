import requests
import socket

def getResults(what=None, where=None):
    starts = "http://api.sandbox.yellowapi.com"
    business = '/FindBusiness/?'
    apikeys = "gs8tzkby7anduedwey5jtf6s"
    whats = "restaurants" if what is None else what
    wheres = "Montreal" if where is None else where
    UIDs = socket.gethostbyname(socket.gethostname())

    payload = {'what': whats, 'where': wheres, 'pgLen': 3,
               'fmt': 'JSON', 'UID': UIDs, 'apikey': apikeys}

    r = requests.get(starts + business, params=payload)

    output = r.json()
    for i in range(3):
        location = output['listings'][i]['name']

        print(location)
        # Open the URL in a new tab
