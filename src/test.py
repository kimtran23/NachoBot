import requests

starts = "http://api.sandbox.yellowapi.com"
business = '/FindBusiness/?'
apikeys = "gs8tzkby7anduedwey5jtf6s"
whats = "restaurants"
wheres = "toronto"
UIDs = "132.205.229.134"

#listing = "/FindBusiness/?what={what}&{where}&fmt=JSON&UID={UID}&apikey={apikey}"
#listing = listing.format(what=whats, where=wheres, UID=UIDs, apikey=apikeys)
payload = {'what': whats, 'where' : wheres, 'fmt': 'JSON', 'UID': UIDs, 'apikey': apikeys}
r = requests.get(starts+business, params=payload)
print(r.url)
