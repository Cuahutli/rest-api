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


def create_update():
    new_data = {
        "user":1,
        "content": "Todavía mejor y cool Otra gran actualización"
    }
    r = requests.post(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

#print(get_list())
#print(create_update())

def do_obj_update():
    new_data = {
        "content": "Nuevo dato de objeto"
    }
    r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    
    # new_data = {
    #     "id":1,
    #     "content": "Todavía mejor y cool Otra gran actualización"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.json())
    # print(r.hedaers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        "content": "Nuevo dato de objeto"
    }
    r = requests.delete(BASE_URL + ENDPOINT + "1/")
    
    # new_data = {
    #     "id":1,
    #     "content": "Todavía mejor y cool Otra gran actualización"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.json())
    # print(r.hedaers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

print(do_obj_update())
print(do_obj_delete())