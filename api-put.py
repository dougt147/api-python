#!/usr/bin/env python3

# PUT - update an existing entry on the endpoint.
# NOTE: Completely overwrites the endpoint data - if you don't specify a k/v pair, it will be deleted
# So do a GET first to see what the data looks like, then you know what to have in your PUT request.
# If you want to just update specific values, use PATCH instead.

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

payload ={
    'userId': 1,
    'title': 'do stuff with things', 
    'completed': False
    }

response = requests.get(api_url)
print(response.json())
print("Return code GET:  " + str(response.status_code))

response = requests.put(api_url,json=payload)
    
print(response.json())
print("Return code PUT " + str(response.status_code))


