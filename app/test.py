import requests
import os
import pathlib
from zipfile import ZipFile
import json


def test():
    BASE_DIR = pathlib.Path(__file__).parent.absolute()
    file = os.path.join(BASE_DIR, 'json', 'urls.zip')
    path_to_unzip = os.path.join(BASE_DIR, 'json')
    zipfile = ZipFile(file)
    zipfile.extractall(path=path_to_unzip)
    with open(os.path.join(path_to_unzip, 'urls.json'), 'r') as f:
        json_file = json.loads(f.read())
    for i in json_file:
        response = requests.get(i)
        content = response.content
        count = content.find(b'Not Found')
        count2 = content.find(b'not found')
        count3 = content.find(b'NOT FOUND')
        count4 = content.find(b'404 Not Found')
        if response.status_code == 404:
            requests.post('https://37.120.146.81/travis/', json=json.dumps({i: json_file[i]}), verify=False)
        elif count > 0 or count2 > 0 or count3 > 0 or count4 > 0:
            requests.post('https://37.120.146.81/travis/', json=json.dumps({i: json_file[i]}), verify=False)
        else:
            pass

