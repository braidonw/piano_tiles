from directKeys import click, queryMousePosition
from screengrab import is_pixel_below_threshold
import time


game_pixels = [(2780, 300), (2860, 300), (3000, 300), (3140, 300)]


def click_black_pixel(x, y, y_offset):
    click(x, y + y_offset)


def check_out_of_bounds():
    return queryMousePosition().x < game_pixels[0][0]


def play_game():
    ''' play the game '''
    i = 0
    y_offset = 0
    start_time = time.time()
    while True:
        for (x, y) in game_pixels:
            below_threshold, elapsed_time = is_pixel_below_threshold(x, y, 100)
            if below_threshold:
                time_adj = int(round(((time.time() - start_time) * 1500)))
                y_offset_used = time_adj + y_offset
                click_black_pixel(x, y, min(y_offset_used, 500))
                i += 1
                if i % 10 == 0:
                    y_offset += 1
                start_time = time.time()
        if check_out_of_bounds():
            break


def click_start_button():
    for (x, y) in game_pixels:
        click(x, y+300)


if __name__ == '__main__':
    click_start_button()
    play_game()
