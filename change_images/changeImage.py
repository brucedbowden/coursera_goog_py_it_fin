#!/usr/bin/env python3

import os, sys, re
from PIL import Image
images_path = './files/'

def change_files(images_path):
    for f in os.listdir(images_path):
        if f == 'README' or f == 'LICENSE':
            continue
        newf = re.sub(r'\..*$', '.jpg', f)
        im = Image.open(os.path.join(images_path, f)).convert('RGB')
        im = im.resize((600, 400))
        im.convert('RGB')
        im.save(os.path.join(images_path, newf), 'JPEG')

def main(argv):
    change_files(argv[1])

if __name__ == "__main__":
    main(sys.argv)
