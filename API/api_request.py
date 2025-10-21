"""
api_request.py
----------------
A Python script to demonstrate GET and POST API calls using the requests library.
"""

import requests

def print_responses(response_data):
    print("Complete response\n{")
    if isinstance(response_data, list):
        for res in response_data:
            print(" {")
            for key,value in res.items():
                if isinstance(value, str):
                    value = value.strip().replace('\n', ' ')
                print(f"    {key} : {value}")
            print(" },")

    elif isinstance(response_data, dict):
        for key,value in response_data.items():
            if isinstance(value, str):
                value = value.strip().replace('\n', ' ')
            print(f"    {key} : {value}")

    else:
        print("Unexcepted response format")
    print('}')

#Get reponse from server via API
url = "https://jsonplaceholder.typicode.com/posts/"
params = {"userId": 1}
print("Get method")
response = requests.get(url, params=params)
data1 = response.json()

print("Get Response Status :", response)
print_responses(data1)



#Post payload to server and get response
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learn Python APIs",
    "body": "APIs are awesome!",
    "userId": 1
    }
print("\nPost method")
response = requests.post(url, json=payload)
data2 = response.json()

print("Post Response Status :", response.status_code)
print_responses(data2)

