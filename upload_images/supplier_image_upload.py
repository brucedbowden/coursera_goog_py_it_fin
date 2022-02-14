#!/usr/bin/env python3

import os, sys
import requests

def upload_images(url, dir):
#    print(dir)
    for f in os.listdir(dir):
        if f == dir of f == 'README' or f == 'LICENSE' or 'tiff' in f:
            continue
        print(dir, f, os.path.join(dir, f))
        with open(os.path.join(dir, f), 'rb') as file:
            response = requests.post(url, files={'file': file})
            print('Response ', f, ':', response.status_code)

def main(argv):
    url = 'http://localhost/upload/'
    upload_images('url', argv[1])

if __name__ == "__main__":
    main(sys.argv)