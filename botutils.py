import cv2
import numpy as np
import pyautogui as gui

from time import sleep

def findTempl(_template_name, _threshold, _region):

    screen = gui.screenshot(region=_region)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGRA)

    templ = cv2.imread('templates/'+_template_name+'.png', cv2.IMREAD_UNCHANGED)
    rectangles = []

    result = cv2.matchTemplate(screen, templ, cv2.TM_CCOEFF_NORMED)
    ypos, xpos = np.where(result >= _threshold)
    height, width = templ.shape[:2]
    for (x, y) in zip(xpos,ypos):
        rectangles.append([x, y, width, height])
        rectangles.append([x, y, width, height])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.8)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(screen, (x, y), (x+w, y+h), (255,255,255), 2)

    cv2.imshow('View', screen)
    cv2.waitKey(200)

    return rectangles

def foundTempl(_template_name, _threshold, _region):
    rects = findTempl(_template_name, _threshold, _region)
    return len(rects) > 0

def moveMouseFTP(_vec, _durInSec):
    cent = (gui.size()[0]/2, gui.size()[1]/2)
    target = (cent[0] + _vec[0], cent[1] + _cent[1])
    gui.moveTo(traget, _durInSec)

def waitCountdown(_ticks, _interval):
    for i in range(_ticks):
        print(_ticks-i)
        sleep(_interval)

def screamImBotter():
    messages = []
    messages.append("I'm a botter. Report me!")
    messages.append("I use an educational bot for an unfair advantage!")
    messages.append("I run a bot script atm. Report me!")
    messages.append("I'm using a fishing bot, I'm not allowed to.")
    for line in messages:
        gui.press("enter")
        for char in line:
            gui.press(char)
        gui.press(enter)
