import json
import urllib
import urllib2
import json
import desktop
import os

with open('desktopsettings.json', 'rb') as fp:
	data = json.load(fp)
mod1 = bool(data['module1'])
mod2 = bool(data['module2'])
mod3 = bool(data['module3'])
