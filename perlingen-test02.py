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

def roughnoise(img: Image, img2=None):
    for x in range(IMG_SIZE):
        for y in range(IMG_SIZE):

            pixels = [
                img.getpixel(((x-1) % IMG_SIZE, (y-1) % IMG_SIZE)),
                img.getpixel(((x) % IMG_SIZE, (y-1) % IMG_SIZE)),
                img.getpixel(((x+1) % IMG_SIZE, (y-1) % IMG_SIZE)),
                img.getpixel(((x-1) % IMG_SIZE, (y) % IMG_SIZE)),
                img.getpixel(((x) % IMG_SIZE, (y) % IMG_SIZE)),
                img.getpixel(((x+1) % IMG_SIZE, (y) % IMG_SIZE)),
                img.getpixel(((x-1) % IMG_SIZE, (y+1) % IMG_SIZE)),
                img.getpixel(((x) % IMG_SIZE, (y+1) % IMG_SIZE)),
                img.getpixel(((x+1) % IMG_SIZE, (y+1) % IMG_SIZE))
            ]

            rpixel = ( (random.choice(pixels)[0] + random.randint(-5, 5) * random.choice([0,0,0,0,0,1,1,2,2])) )   % 255
            
            color = (rpixel, rpixel, rpixel)
            

            img.putpixel((x,y), color)
            for i in range(0, random.randint(0, 10)):
                img.putpixel(((x+i) % IMG_SIZE,y), color)
                img.putpixel((x,(y+i) % IMG_SIZE), color)
                img.putpixel(((x-i) % IMG_SIZE,y), color)
                img.putpixel((x,(y-i) % IMG_SIZE), color)

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

img = make_image()
roughnoise(img=img)
img.save(IMG_NAME)
#fader(img=img, img2=None)
#img.save(IMG_NAME)
img.show()