import urllib
import urllib2
import json
import desktop
import user

username = 'GavinGu'
password = 'pepper1234'

url = 'http://localhost:8000/desktopsettings/'

values = {'username' : username, 'password' : password}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
test = json.load(response)

with open('desktopsettings.json', 'wb') as fp:
	json.dump(test, fp)

