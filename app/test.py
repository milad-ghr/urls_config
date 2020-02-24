import requests
from requests import exceptions
import os
from zipfile import ZipFile
import json

from json_folder import BASE_DIR


def request(data, json_file, counter):
    for i in data:
        try:
            response = requests.get(i, timeout=10)
        except exceptions.ConnectionError:
            requests.post('https://37.120.146.81/travis/',
                          json=json.dumps({i: json_file[i], 'type': 'ConnectionError'}),
                          verify=False)
            continue
        content = response.content
        count = content.find(b'Not Found')
        count2 = content.find(b'not found')
        count3 = content.find(b'NOT FOUND')
        count4 = content.find(b'404 Not Found')
        if response.status_code == 404:
            requests.post('https://37.120.146.81/travis/',
                          json=json.dumps({i: json_file[i], 'type': '404'}),
                          verify=False)
        elif count > 0 or count2 > 0 or count3 > 0 or count4 > 0:
            requests.post('https://37.120.146.81/travis/',
                          json=json.dumps({i: json_file[i], 'type': 'not_found'}),
                          verify=False)
        else:
            pass
        print(f'Done url {i} in range gt {counter}')


def test():
    file = os.path.join(BASE_DIR, 'urls.zip')
    path_to_unzip = os.path.join(BASE_DIR)
    zipfile = ZipFile(file, 'r')
    zipfile.extractall(path=path_to_unzip)
    with open(os.path.join(path_to_unzip, 'urls.json'), 'r') as f:
        json_file = json.loads(f.read())
    urls = list(json_file.keys())
    counter = 0
    for data in range(0, len(urls), 500):
        if data > 360000:
            request(urls[counter:len(urls)], json_file, counter)
        else:
            request(urls[counter:data], json_file, counter)
            counter += data
        print(f'done from {counter} to {data}')
    return 'done'



