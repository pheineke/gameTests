import random
import time
from PIL import Image, ImageDraw

IMG_SIZE = 1000
IMG_NAME = 'sqr.png'

def make_image() -> Image:
    img = Image.new('RGB', (IMG_SIZE, IMG_SIZE), color = 'white')
    img.save(IMG_NAME)
    return img

def read_image() -> Image:
    img = Image.open(IMG_NAME)
    return img

def roughnoise(img: Image, img2):
    for x in range(IMG_SIZE):
        for y in range(IMG_SIZE):
            x = x * 10 % IMG_SIZE
            y = y * 10 % IMG_SIZE
            z = random.randint(0, 255)
            color = (z, z, z)
            print(color)
            img.putpixel((x,y), color)


def roughnoise2(img: Image, img2):
    for i in range(IMG_SIZE*IMG_SIZE):
        x = random.randint(0, IMG_SIZE)
        y = random.randint(0, IMG_SIZE)
        z = random.randint(0, 255)
        color = (z, z, z)

        img2.rectangle([x, y, x+random.randint(0,50),y+random.randint(0,50)], fill=color)
    

def fader(img, img2):
    for x in range(IMG_SIZE):
        for y in range(IMG_SIZE):

            pixel = img.getpixel((x,y))[0]
            print(pixel, x,y, (x+1) % IMG_SIZE, (y+1) % IMG_SIZE)
            pixel0 = img.getpixel((x,(y-1) % IMG_SIZE))[0]
            pixel1 = img.getpixel(((x-1) % IMG_SIZE,y))[0]
            pixel2 = img.getpixel(((x+1) % IMG_SIZE,y))[0]
            pixel3 = img.getpixel((x,(y+1) % IMG_SIZE))[0]

            avg = ((pixel + pixel0 + pixel1 + pixel2 + pixel3) // 3) % 255
            
            img.putpixel((x,y), (avg, avg, avg))

def zeroer(img, img2):
    for x in range(IMG_SIZE):
        for y in range(IMG_SIZE):
            if (img.getpixel((x,y))[0] < 200):
                img.putpixel((x,y), (0,0,0))

img = make_image()
img2 = ImageDraw.Draw(img)
roughnoise2(img, img2)
zeroer(img, img2)
fader(img, img2)
img.save(IMG_NAME)

