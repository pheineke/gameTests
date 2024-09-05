import random
import time
from PIL import Image, ImageDraw

IMG_SIZE = 1000

IMG_GRID = []

IMG_NAME = 'sqr.png'

def make_image() -> Image:
    img = Image.new('RGB', (IMG_SIZE, IMG_SIZE), color = 'white')
    img.save(IMG_NAME)
    return img

def read_image() -> Image:
    img = Image.open(IMG_NAME)
    return img

def grid_to_image():
    img = read_image()
    img2 = ImageDraw.Draw(img)
    for i in range(IMG_SIZE):
        for j in range(IMG_SIZE):
            value = int(IMG_GRID[i][j] * 255)
            color = (value, value, value)
            img2.point((i, j), fill = color)
        
    img.save(IMG_NAME)
    return img


def generate_imagegrid():
    for i in range(IMG_SIZE):
        IMG_GRID.append([])
        for j in range(IMG_SIZE):
            IMG_GRID[i].append(0)

def randompixel():
    for i in range(IMG_SIZE):
        for j in range(IMG_SIZE):
            IMG_GRID[i][j] = random.random()

def add_random():
    for i in range(IMG_SIZE):
        for j in range(IMG_SIZE):
            IMG_GRID[i][j] += random.random()




def main():
    generate_imagegrid()
    
    randompixel()
    for i in range(3):
        add_random()

    IMG = grid_to_image()


main()


