import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time

gameCoords = [2672, 160, 3268, 1030]

score = 0
previousLane = -1


def clickOnFirstBlock(screen):
    global gameCoords, score, previousLane
    for y_ in range(5, len(screen) - 5, 5):
        for i in range(4):
            if previousLane == i:
                continue
            w = gameCoords[2] - gameCoords[0]
            x = int(round(i * w / 4 + w / 8))
            y = len(screen) - y_
            if screen[y][x] < 50:
                actualX = x + gameCoords[0]
                actualY = y + gameCoords[1]
                score += 1
                if score > 500:
                    actualY += 45
                if score > 700:
                    actualY += 15
                if score > 800:
                    actualY += 20
                if score > 900:
                    actualY += 20
                if score > 1100:
                    actualY += 20
                if score > 1200:
                    actualY += 30
                if score > 1350:
                    actualY += 25
                if score > 1600:
                    actualY += 30
                if score > 1700:
                    actualY += 35
                if score > 1800:
                    actualY += 55
                if score > 1900:
                    actualY += 65
                if score > 2000:
                    actualY += 65
                for k in range(1900, 2500):
                    if score > k:
                        actualY += 20
                    else:
                        break
                click(actualX, actualY)
                previousLane = i
                return


def safeguard():
    mousePos = queryMousePosition()
    return mousePos.x > gameCoords[0]


def start_the_game():
    for x in [2720, 2860, 3000, 3140]:
        click(x, 600)


def play_the_game():

    startTime = time.time()
    # print(startTime)
    screen = np.array(ImageGrab.grab(bbox=gameCoords))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    clickOnFirstBlock(screen)
    # print("Frame took {} seconds. Up to frame no {}".format(
    #     (time.time() - startTime), "FUCK YOU"))
    # else:
    #     if mousePos.x < 0:
    #         score = 0
    #         while True:
    #             mousePos = queryMousePosition()
    #             if gameCoords[2] < mousePos.x:
    #                 break


if __name__ == '__main__':
    start_the_game()
    while safeguard() is True:
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=gameCoords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        clickOnFirstBlock(screen)
        # print("Frame took {} seconds. Up to frame no {}".format(
        #     (time.time() - startTime), "FUCK YOU"))
