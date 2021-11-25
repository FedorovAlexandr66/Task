from PIL import Image
import numpy as np
from numpy import array


def get_grayrate(x, y):
    gray = 0
    for windows_x in range(x, min(x + width_img // width_mosaic, width_img)):
        for windows_y in range(y, min(y + height_img // height_mosaic, height_img)):
            R = img_arr[windows_x][windows_y][0]
            G = img_arr[windows_x][windows_y][1]
            B = img_arr[windows_x][windows_y][2]
            gray += (int(R) + int(G) + int(B)) / 3
    return int(gray // 100)


def make_chunk_grey_pictures(x, y, grayrate):
    for windows_X in range(x, min(x + width_img // width_mosaic, width_img)):
        for windows_Y in range(y, min(y + height_img // height_mosaic, height_img)):
            img_arr[windows_X][windows_Y] = [int(grayrate // 50 * grayrate_step) * grayrate_step * 50] * 3
    return img_arr


def make_grey_pictures():
    global img_arr
    x = 0
    while x < width_img - 1:
        y = 0
        while y < height_img - 1:
            grayrate = get_grayrate(x, y)
            img_arr = make_chunk_grey_pictures(x, y, grayrate)
            y = y + width_img // width_mosaic
        x = x + height_img // height_mosaic
    res = Image.fromarray(img_arr)
    res.save(result_file)


print("напишите раположение файла в полной форме")
file = input()
print("напишите раположение результирующего файла в полной форме")
result_file = input()
img_arr = array(Image.open(file))
width_img = len(img_arr)
height_img = len(img_arr[1])
print("напишите ширину мозаики")
width_mosaic = int(input())
print("напишите высоту мозаики")
height_mosaic = int(input())
print("напишите шаг градации серого")
grayrate_step = int(input())
make_grey_pictures()
