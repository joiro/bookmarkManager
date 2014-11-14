import urllib, json
url = "http://data.nottinghamtravelwise.org.uk/parking.json?noLocation=true?t=635509084580321642"
response = urllib.urlopen(url);
data = json.loads(response.read())
print data
