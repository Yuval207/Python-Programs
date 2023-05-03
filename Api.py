import requests
import json

r = requests.get('https://api.nasa.gov/planetary/apod', params = {"api_key" : "DEMO_KEY"})
print(r.url)