import json

def get_all_stadiums():
    with open('stadiums.json', 'r') as f:
        s = f.read()
        j = json.loads(s)
        return j
