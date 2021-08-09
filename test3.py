#!/usr/bin/env python3
import requests

url = 'https://abababababababsss.com'

response = requests.get(url)

if not response.ok:
    #raise Exception("GET failed with status code {}".format(response.raise_for_status()))
     print(response.raise_for_status())

else:
    print(response.status_code)