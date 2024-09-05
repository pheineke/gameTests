
import math
import random
import time
from PIL import Image, ImageDraw


GRID_SIZE = 100

GRID = []

def make_grid():
    for i in range(GRID_SIZE):
        GRID.append([])
        for j in range(GRID_SIZE):
            GRID[i].append(None)

POINTS = []

def draw_points():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if i % 10 == 0 and j % 10 == 0:
                GRID[i][j] = random.randint(0, 255)
                POINTS.append((i, j))

I = 0
def image_name():
    global I
    name = f'gifer/grid_{I}.png'
    I += 1
    return name

def grid_to_image():
    img = Image.new('RGBA', (GRID_SIZE, GRID_SIZE), color = (255, 255, 255, 0))
    img2 = ImageDraw.Draw(img)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid_value = GRID[i][j]
            if grid_value:
                img2.point((i, j), fill = (grid_value, grid_value, grid_value, 255))

    img.save(image_name())

def main():
    make_grid()
    draw_points()
    grid_to_image()

if __name__ == '__main__':
    i = 0
    while(i < 10):
        main()
        i += 1

    #all images to gif:
    import os
    os.system('convert -delay 100 gifer/grid_*.png gifer/grid.gif')
    os.system('rm gifer/grid_*.png')
