import requests
import webbrowser
import socket
import tweepySetup
import textparser

starts = "http://api.sandbox.yellowapi.com"
business = '/FindBusiness/?'
apikeys = "gs8tzkby7anduedwey5jtf6s"
whats = "restaurants"
wheres = "Montreal"
UIDs = socket.gethostbyname(socket.gethostname())

payload = {'what': whats, 'where': wheres, 'pgLen':3,
           'fmt': 'JSON', 'UID': UIDs, 'apikey': apikeys}

r = requests.get(starts + business, params=payload)

output = r.json()
for i in range(3):
    location = output['listings'][i]['name']

    print(location)
# Open the URL in a new tab
