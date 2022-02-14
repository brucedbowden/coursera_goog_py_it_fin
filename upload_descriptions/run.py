#!/usr/bin/env python3

import os, sys
import requests
import json

def upload_descriptions(url, dir):
    for f in os.listdir(dir):
        i = f.replace('txt', 'jpeg')
        print(i)
        with open(os.path.join(dir, f), 'r') as desc:
            lines = desc.read().strip().splitlines()
            dict = {"name": lines[0], "weight": lines[1].replace(' lbs', ''), "description": lines[2], "image": i}
            # json_string = json.dumps(dict)
            print(json_stringct)
            response = requests.post('http://localhost/fruits', data=dict)
           print(response.status_code)

def main(argv):
    upload_descriptions('http://34.134.225.136/fruits', argv[1])

if __name__ == "__main__":
    main(sys.argv)