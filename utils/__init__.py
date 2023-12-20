import json

def load(dataJson):
    data, error = [], None
    try:
        with open (dataJson, "r") as file:
            data = json.load(file)
    except IOError as e:
        error = e
    return data, error

def store(data, dataJson):
    try:
        list_Penampung = json.dumps(data, indent=4)
        with open (dataJson, 'w') as file:
            file.write(list_Penampung)
        return True
    except IOError as e:
        print(e)
        return False
