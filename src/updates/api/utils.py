import json

def is_json(json_data):
    try:
        real_json = json.loads(json_data.decode('utf-8'))
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid
