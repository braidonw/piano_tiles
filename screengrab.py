from ctypes import *
import time


user = windll.LoadLibrary("c:\\windows\\system32\\user32.dll")
h = user.GetDC(0)
gdi = windll.LoadLibrary("c:\\windows\\system32\\gdi32.dll")


dc = windll.user32.GetDC(0)


def get_pixel(x, y):
    return windll.gdi32.GetPixel(dc, x, y)


def is_below_threshold(pixel, threshold):
    """ Pixel is 0xRRGGBB or 0xBBGGRR """
    green = (pixel >> 8) & 255
    red = (pixel >> 16) & 255  # legit not sure if red but doesn't fucking matter
    blue = (pixel >> 0) & 255  # legit not sure if blue but doesn't fucking matter
    return green < threshold and red < threshold and blue < threshold


def is_pixel_below_threshold(x, y, threshold):
    start_time = time.time()
    below_threshold = is_below_threshold(get_pixel(x, y), threshold)
    elapsed_time = time.time() - start_time
    return below_threshold, elapsed_time


if __name__ == '__main__':
    pixel = get_pixel(2460, 800)
    print(is_below_threshold(pixel, 50))

    pixel_2 = get_pixel(2, 2)
    print('what about the other one: {}'.format(is_below_threshold(pixel_2, 50)))
