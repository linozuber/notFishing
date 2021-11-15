import cv2
import numpy as np
import pyautogui as gui

from time import sleep
from random import random, choice

def findTempl(_template_name, _threshold, _region):
    xx = _region[0]
    yy = _region[1]
    ww = _region[2]
    hh = _region[3]

    screen = gui.screenshot(region=(xx,yy,ww,hh))
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

class fisher():
    INITIALIZE, CASTING, WAITING, WINDING, LOOSENING = 0,1,2,3,4
    state = INITIALIZE

    def __init__(self):
        pass

    def goFishing(self):
        size = gui.size()
        ww = size[0]/4
        hh = size[1]*0.8
        xx = size[0]/2 - ww/2
        yy = size[1]/2 - hh/2

        while True:
            if self.state == self.INITIALIZE:
                print("5")
                sleep(1)
                print("4")
                sleep(1)
                print("3")
                sleep(1)
                print("2")
                sleep(1)
                print("1")
                sleep(1)
                print("0")
                self.state = self.CASTING
            if self.state == self.CASTING:
                gui.mouseDown()
                sleep(choice([1.2,1.5,1.8,2.1,2.4]))
                gui.mouseUp()
                sleep(2.5)
                if foundTempl("bobber", 0.8 ,(xx,yy,ww,hh)):
                    self.state = self.WAITING
            if self.state == self.WAITING:
                if foundTempl("hooked", 0.75 ,(xx,yy,ww,hh)):
                    gui.click()
                    self.state = self.LOOSENING
            if self.state == self.WINDING:
                if foundTempl("highten", 0.8 ,(xx,yy,ww,hh)):
                    gui.mouseUp()
                    self.state = self.LOOSENING
            if self.state == self.LOOSENING:
                if foundTempl("lowten", 0.8 ,(xx,yy,ww,hh)):
                    gui.mouseDown()
                    self.state = self.WINDING
            if self.state == self.WINDING or self.state == self.LOOSENING:
                if foundTempl("success", 0.7 ,(xx,yy,ww,hh)):
                    gui.mouseUp()
                    self.state = self.INITIALIZE

fisherman = fisher()
fisherman.goFishing()
