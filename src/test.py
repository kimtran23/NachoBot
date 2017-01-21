import requests
import webbrowser

starts = "http://api.sandbox.yellowapi.com"
business = '/FindBusiness/?'
apikeys = "gs8tzkby7anduedwey5jtf6s"
whats = "restaurants"
wheres = "-79.390898, 43.67057"
UIDs = "132.205.229.134"

# listing = "/FindBusiness/?what={what}&{where}&fmt=JSON&UID={UID}&apikey={apikey}"
# listing = listing.format(what=whats, where=wheres, UID=UIDs, apikey=apikeys)
payload = {'what': whats, 'where': wheres,
           'fmt': 'JSON', 'UID': UIDs, 'apikey': apikeys}

r = requests.get(starts + business, params=payload)
# Open the URL in a new tab
webbrowser.open_new_tab(r.url)
