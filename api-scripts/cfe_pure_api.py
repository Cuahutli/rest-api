import requests #http requests
import json

BASE_URL = "http://localhost:8000/"

ENDPOINT = "api/updates/"
def get_list(id=None): # Lists all this out
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print('Algo salió mal')
    data = r.json()
    return data


def create_update():
    new_data = {
        "user":1,
        "content": "Todavía mejor y cool Otra gran actualización"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

print(get_list())
#print(create_update())

def do_obj_update():
    new_data = {
        "id": 5,
        "content": "Nuevo dato de objeto maravilloso"
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    

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
        "id": 5,
        "content": "Nuevo dato de objeto"
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    
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

#print(do_obj_update())
#print(do_obj_delete())