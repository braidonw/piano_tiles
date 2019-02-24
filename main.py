import time
import numpy as np
import cv2
from PIL import ImageGrab
import keyboard
from directKeys import click, queryMousePosition, moveMouseTo
from mss import mss
#Game coords are the coords of the game window
#   when placed in the top right of the screen
GAME_COORDS = (2700, 800, 3240, 801)

# We need to only check 4 columns of pixels for a black pixel
# checking the whole area only gives ~10fps - we want more than that!
COL1_COORDS = (2720 - GAME_COORDS[0], 800 - GAME_COORDS[1], 2721 - GAME_COORDS[0], 801 - GAME_COORDS[1])
COL2_COORDS = (2860 - GAME_COORDS[0], 800 - GAME_COORDS[1], 2861 - GAME_COORDS[0], 801 - GAME_COORDS[1])
COL3_COORDS = (3000 - GAME_COORDS[0], 800 - GAME_COORDS[1], 3001 - GAME_COORDS[0], 801 - GAME_COORDS[1])
COL4_COORDS = (3140 - GAME_COORDS[0], 800 - GAME_COORDS[1], 3141 - GAME_COORDS[0], 801 - GAME_COORDS[1])

COLUMNS_TO_CHECK = [COL1_COORDS, COL2_COORDS, COL3_COORDS, COL4_COORDS]

def do_click(_x, _y):
    click(_x, _y)

def find_a_tile(area, col):
    """find a tile in the given area"""
    for _y in range(col[1], col[3]):
        for _x in range(col[0], col[2]):
            if area[_y][_x] < 20:   
                print('found blak pixel at {}, {}'.format(_x, _y))
                return True, _x, _y
    return False, None, None


def look_at_the_game(col_coords, sct):
    """look at the game"""
    screen = np.array(sct.grab(col_coords))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    return screen


def play_the_game(columns, sct, y_offset):
    """play the game with given columns. lolwut"""
    area = look_at_the_game(col_coords=GAME_COORDS,sct=sct)
    for col in columns:
        found, _x, _y = find_a_tile(area=area, col=col)
        if found:
            do_click(GAME_COORDS[0] + _x, GAME_COORDS[1] + _y - y_offset)
            print('clicked {}, {}'.format(GAME_COORDS[0] + _x, GAME_COORDS[1] + _y - y_offset))
            return

def start(columns):
    """starts the game with given columns"""
    for col in columns:
        _x, _y = col[0], (col[3]-300)
        do_click(GAME_COORDS[0]+_x, GAME_COORDS[1]+_y)

def check_out_of_bounds():
    return queryMousePosition().x < GAME_COORDS[0]

last_time = time.monotonic_ns()

def print_frame_time():
    global last_time
    current_time = time.monotonic_ns()
    delta_time = current_time - last_time
    print(delta_time/1000000)
    last_time = current_time
    return print_frame_time

def run():
    start(COLUMNS_TO_CHECK)
    with mss() as sct:
        #i = 0
        y_offset = 0
        while True:
           # if i % 5000 == 0:
             #   y_offset += 1
            #print_frame_time()
            play_the_game(COLUMNS_TO_CHECK, sct, y_offset)
            # stime.sleep(16/1000)
            #print("i = {} - y_offset = {}".format(i, y_offset))
            if check_out_of_bounds():
                break
           # i+=1

if __name__ == '__main__':
    run()
   
