import requests #http requests
import json

BASE_URL = "http://localhost:8000/"

ENDPOINT = "api/updates/"
def get_list(): # Lists all this out
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    data = r.json()
    print(type(data))
    print(type(json.dumps(data)))
    for obj in data:
        #print(obj['id'])
        if obj['id'] == 1: #--> User interaction
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            #print(dir(r2))
            print(r2.json())
    return data


get_list()