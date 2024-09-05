import random
import time
from PIL import Image, ImageDraw


IMG_SIZE = 100

IMG_GRID = []

IMG_NAME = 'sqr.png'


def get_points():
    points = []
    
    points_2 = []

    for i in range(random.randint(10, 50)):
        x = random.randint(0, IMG_SIZE)
        y = random.randint(0, IMG_SIZE)

        points.append((x, y))

        a = random.randint(x-10, x+10)
        b = random.randint(y-10, y+10)

        points_2.append((a, b))

    return points, points_2

def make_image() -> Image:
    for i in range(IMG_SIZE):
        IMG_GRID.append([])
        for j in range(IMG_SIZE):
            IMG_GRID[i].append(0)

    img = Image.new('RGB', (IMG_SIZE, IMG_SIZE), color = 'white')
    img.save(IMG_NAME)
    return img

def read_image() -> Image:
    img = Image.open(IMG_NAME)
    return img

def draw_points():
    points, points_2 = get_points()

    img = read_image()
    img2 = ImageDraw.Draw(img)
    for i in range(len(points)):
        point_i = points[i]
        point_i_2 = points_2[i]

        print(point_i, point_i_2)

        #IMG_GRID[point_i[0]][point_i[1]] = 1
        #IMG_GRID[point_i_2[0]][point_i_2[1]] = -1

        img2.point((point_i[0], point_i[1]), fill = 'black')
        img2.point((point_i_2[0], point_i_2[1]), fill = 'red')

        #img2.point(point_i, fill = 'black')
        #img2.point(point_i_2, fill = 'red')
        
    img.save(IMG_NAME, 'PNG')
    return img

def fader(t):
    return ((6*t - 15)*t + 10)*t*t*t


make_image()
draw_points()
