import requests
import json


URL = 'http://127.0.0.1:8000'
def get(id=None):
    if id is not None:
        data = {
            'id':id,
        } 
        json_data = json.dumps(data)
        headers = {'content-Type':'application/json'}
        r = requests.get(URL, headers=headers, data=json_data)
        json_data = r.json()
        print(json_data)

def post():
    data = {
        'name':'Hulk',
        'user_num':3,
        'email':'hulk',
        'password':'hulk@123'
    }

    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    r = requests.post(URL, headers=header, data=json_data)
    json_data = r.json()
    print(json_data)

def put():
    data = {
        'id':20,
        'name':'Naruto',
        'user_num':2,
        'email':'naruto@gmail.com',
        'password':'naruto@123'
    }
    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    r = requests.put(URL, headers=header, data=json_data)
    json_data = r.json()
    print(json_data)

def delete(id):
    data = {
        'id':id
    }
    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    r = requests.delete(URL, headers=header, data=json_data)
    json_data = r.json()
    print(json_data)

id = input()
get(id)
# post()
# put()
# delete(id)