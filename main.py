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


def get_time(url):
    params = {'X-Api-Key': get_api_key(), 'hydrated': 'true'}

    p = requests.get(url=url2, headers=params)

    d = p.json()
    polo =[]
    id_arr=['']

    k=d['timeentries']
    for i in k:
        polo.append(i['taskName'])
        polo.append(i['timeInterval'])

    return polo

def time_function(x):
    h=x//3600
    m=x//60%60
    s=x%60
    return str(h) +':'+ str(m) +':'+ str(s)



def make_list(d):
    final_list = [0] * len(d)
    for i in range(0, len(d), 2):
        final_list[i] = d[i]
    for i in range(1, len(d), 2):
        final_list[i] = [d[i]['start'][0:10], d[i]['duration']]

    k = True
    x = 0
    while k:
        if (x == len(final_list)):
            k = False
            break
        l = final_list[x]
        for j in range(x + 1, len(final_list) - 1):
            if final_list[j] == l:
                del final_list[j]
                final_list.insert(j, ['', 0])
        x = x + 1
    i=1
    while(i<len(final_list)):
        if final_list[i][0]=='':
            final_list[i][1]=final_list[i-1][1]+final_list[i+1][1]
            final_list[i][0]=final_list[i-1][0]+' - ' +final_list[i+1][0]
            t = True
            r = i
            while t:
                if final_list[r+2][0] == '':
                    final_list[i][1] = final_list[i][1] + final_list[r+1][1]
                    final_list[i][0] = final_list[i][0] +' - '+ final_list[r + 1][0]
                    r = r+2
                else:
                    t = False
                    i=r
        i=i+1

    for i in range(1, len(final_list)):
        if final_list[i][0][0:4]=='2022':
            final_list[i][1]=time_function(final_list[i][1])
    return final_list




url1='https://api.clockify.me/api/v1/workspaces/6283b75fe6e6df296e95c2ee/projects/6283b789e6e6df296e95c64f/tasks'
url2='https://reports.api.clockify.me/v1/shared-reports/6284e8bb5a779e7a4db678cd'

d=get_time(url2)

x=make_list(d)

#print(x) #для вивода розкоментуйте
