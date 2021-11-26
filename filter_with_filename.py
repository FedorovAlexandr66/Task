from PIL import Image
import numpy as np
from numpy import array


def get_grayrate(x, y):
    """Вычимсляет оттенок серого цвета по полученным координатам
    :param x: координата по оси X
    :param y: координата по оси Y
    :return: оттенок серого цвета

    >>> get_grayrate(0,75)
    4275
    >>> get_grayrate(225,375)
    14062

    """
    gray = 0
    for windows_x in range(x, min(x + width_img // width_mosaic, width_img)):
        for windows_y in range(y, min(y + height_img // height_mosaic, height_img)):
            R = img_arr[windows_x][windows_y][0]
            G = img_arr[windows_x][windows_y][1]
            B = img_arr[windows_x][windows_y][2]
            gray += (int(R) + int(G) + int(B)) / 3
    return int(gray // 100)


def make_chunk_grey_pictures(x, y, grayrate):
    """Преобразует часть цветов в полученный отенок серого цвета
           :param grayrate: оттенок серого цвета
           :param x: координата по оси X
           :param y: координата по оси Y
           :return: картинка с заменённой частью цветов
        """
    for windows_X in range(x, min(x + width_img // width_mosaic, width_img)):
        for windows_Y in range(y, min(y + height_img // height_mosaic, height_img)):
            img_arr[windows_X][windows_Y] = [int(grayrate // 50 * grayrate_step) * grayrate_step * 50] * 3
    return img_arr


def make_grey_pictures():
    """Делает картинку из оттенков серого цвета
            :return: картинка из оттенков серого цвета
    """
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


file = "C:\\Users\\122\\Desktop\\github\\Task\\img1.jpg"
result_file = "C:\\Users\\122\\Desktop\\github\\Task\\img2.jpg"
img_arr = array(Image.open(file))
width_img = len(img_arr)
height_img = len(img_arr[1])
width_mosaic = 10
height_mosaic = 10
grayrate_step = 10
make_grey_pictures()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
