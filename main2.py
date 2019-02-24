import numpy as np
import cv2 as cv
from PIL import ImageGrab
from directKeys import click, queryMousePosition
from mss import mss


old_game_pixels = {
    'col1': [2720, 400],
    'col2': [2860, 400],
    'col3': [3000, 400],
    'col4': [3140, 400]
}


col_xs = [2780, 2860, 3000, 3140]

pixel1 = [2780, 600, 2782, 601]
pixel2 = [2860, 600, 2862, 601]
pixel3 = [3000, 600, 3002, 601]
pixel4 = [3140, 600, 3142, 601]

game_pixels = [pixel1, pixel2, pixel3, pixel4]

game_pixel_line = [2700, 600, 3140, 601]


def read_pixels(pixel_coords, sct):
    pixel_line = np.array(ImageGrab.grab(bbox=pixel_coords))
    pixel_line = cv.cvtColor(pixel_line, cv.COLOR_BGR2GRAY)
    return pixel_line


def find_black_pixel(pixel_row):
    for pixel in range(len(pixel_row)):
        if pixel_row[pixel] < 30 and pixel_row[(pixel + 1)] < 60:
            return True, pixel
            break
    return False, False


def click_black_pixel(x_offset, y_offset, game_pixel_line=game_pixel_line):
    x = game_pixel_line[0] + x_offset
    y = game_pixel_line[1]
    click(x+50, y-y_offset)


def check_out_of_bounds():
    return queryMousePosition().x < game_pixel_line[0]


def play_game(game_pixel_line=game_pixel_line):
    ''' play the game '''
    i = 0
    with mss() as sct:
        y_offset = 0
        while True:
            pixel_found = False
            pixels = read_pixels(game_pixel_line, sct)
            # print('Pixels: {}'.format(pixels[0]))
            pixel_found, black_pixel = find_black_pixel(pixels[0])
            if pixel_found is True:
                print('''Iteration: {}, black pixel {}, y_offset of {}'''
                      .format(i, black_pixel, y_offset))
                click_black_pixel(black_pixel, y_offset)
                i += 1
                if i % 150 == 0:
                    y_offset -= 25
            if check_out_of_bounds():
                break


def click_start_button(game_pixel_line=game_pixel_line,
                       col_xs=col_xs):
    for i in range(len(col_xs)):
        click(col_xs[i], game_pixel_line[1])


if __name__ == '__main__':
    click_start_button()
    play_game(game_pixel_line)
