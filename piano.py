import numpy as np
from PIL import ImageGrab
import cv2 as cv
import pyautogui as pyag
import time



imgZone = pyag.locateOnScreen('bbox_locator.png', confidence=0.3)
bbox_area = (imgZone[0], imgZone[1], imgZone[0]+imgZone[2],  imgZone[1]+ imgZone[3])
screen = np.array(ImageGrab.grab(bbox=bbox_area))
screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
pyag.click(pyag.locateCenterOnScreen('start_button.png', confidence=0.4))
for i in range(1000):
    startTime = time.time()
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[imgZone[1]+y][imgZone[0]+x] < 1:
                pyag.click(imgZone[0]+x, imgZone[1]+y)
    print("Frame took {} seconds. Up to frame no {}".format((time.time() - startTime), i))

print(screen.shape)

def screen_record(): 
    last_time = time.time()
    while(True):
        # Game window in the top right of the screen
        screen =  np.array(ImageGrab.grab(bbox=game_coords))
        for y in range((len(screen))):
            for x in range(len(screen[0])):
                if screen[y][x] < 1:
                    print(screen[y][x])
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break