import urllib.request
import json

request_url = urllib.request.urlopen('https://bandcamp.com/api/salesfeed/1/get') 
print(request_url.read()) 
