import requests
import os
import pathlib
from zipfile import ZipFile


def test():
    BASE_DIR = pathlib.Path(__file__).parent.absolute()
    file = os.path.join(BASE_DIR, 'json', 'urls.zip')
    path_to_unzip = os.path.join(BASE_DIR, 'json')
    zipfile = ZipFile(file)
    zipfile.extractall(path=path_to_unzip)
    with open(os.path.join(path_to_unzip, 'urls.json'), 'r') as f:
        