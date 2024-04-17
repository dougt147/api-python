#!/usr/bin/env python3
import requests
api_url = "https://jsonplaceholder.typicode.com/todos"

payload ={
    "userId": 1,
    "title": "Test API post request",
    "completed": "False"
}

response = requests.post(api_url,json=payload)
    
print(response.json())
print("Return code " + str(response.status_code))

