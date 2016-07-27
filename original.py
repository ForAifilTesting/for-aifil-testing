'''
Created on Jul 28, 2016

@author: Vladimir
'''

from viewer import Viewer
from PIL import Image
import json
import os
import sys
import requests

png_files = []
image_files = []
api_key = '2902398-0284227c6439d51a2b4352a7c'
img_type = 'green+python'  # то, что ищем


def error(msg='One or more images are not converted'):
    print(msg)
    exit(0)


def convert_images():
    for infile in image_files:
        f, e = os.path.splitext(infile)
        outfile = f + ".png"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
                png_files.append(outfile)
                os.remove(infile)
            except IOError:
                print("cannot convert", infile)


def show_slides():
    viewer = Viewer(png_files)
    viewer.show_slides()
    viewer.run()


def get_images():
    main_url = u'https://pixabay.com/api/?key={}&q={}&image_type=photo=pretty=true'.format(api_key, img_type)
    response = requests.get(main_url).content.decode('utf8')
    hits = json.loads(response)

    directory = 'downloaded_images'
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not hits:
        sys.exit("Found No Images")

    count = 0
    for hit in hits['hits']:
        count += 1
        url = hit['webformatURL']
        res = requests.get(url)
        name = str(count) + '.jpg'
        path = r'downloaded_images/{}'.format(name)
        image_files.append(path)
        f = open(path, 'wb')
        f.write(res.content)
        f.close()


def test():
    get_images()
    convert_images()
    show_slides()


if __name__ == '__main__':
    test()
