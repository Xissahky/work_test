import requests
import json

def get_api_key():
    with open('api_key.txt', 'r') as f:
        return f.read()



def get_list(url):
    params = {'X-Api-Key': get_api_key(), 'hydrated': 'true'}

    p = requests.get(
        url=url,
        headers=params)

    d = p.json()
    polo = []

    for i in d:
        polo.append(i['name'])

    return polo

url1='https://api.clockify.me/api/v1/workspaces/6283b75fe6e6df296e95c2ee/projects/6283b789e6e6df296e95c64f/tasks'

#for i in get_list(url1):  
    #print(i)