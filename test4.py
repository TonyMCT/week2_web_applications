#!/usr/bin/env python3
import requests

#GET method
p = {"search": "grey kitten", "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
print(response.request.url)

#POST method
p2 = {"description": "white kitten","name": "Snowball","age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p2)
print(response.request.url)
print(response.request.body)

#JSON method
response = requests.post("https://example.com/path/to/api", json=p2)
print(response.request.url)
#'https://example.com/path/to/api'
print(response.request.body)
#b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 