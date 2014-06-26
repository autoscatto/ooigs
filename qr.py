from qrcode import *
import Image, ImageOps
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap
import requests
import json

def goo_shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return  r.json().get('id')


font = ImageFont.truetype("./LiberationMono-Regular.ttf",44)
outdir = "./tmp"

def faiesalva(urlo, i):
    URL = goo_shorten_url(urlo)
    qr = QRCode(version=1, error_correction=ERROR_CORRECT_H,  box_size=20)
    qr.add_data(URL)
    qr.make()
    im = qr.make_image()
    im = ImageOps.expand(im,border=(0,50,0,80),fill='white')

    draw = ImageDraw.Draw(im)
    lines = textwrap.wrap(URL, width = 41)
    y_text = 760
    for line in lines:
        width, height = font.getsize(line)
        draw.text((80, y_text), line, font = font, fill = 'black')
        y_text += height
    im = ImageOps.expand(im,border=(0,0,2,2),fill='black')

    im.save("%s/%d.png" %(outdir, i))


f = open("giflist.txt", 'r')
i = 0
for l in f.readlines():
    faiesalva(l, i)
    i += 1
    
