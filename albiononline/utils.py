import cv2
import numpy as np
import pyautogui as pag
import time
import datetime
from math import sqrt
import os
from random import random

def pointDistance(p1, p2):
    xdist = p1[0] - p2[0]
    ydist = p1[1] - p2[1]
    distance = sqrt( pow(xdist,2) + pow(ydist,2) )
    return distance

def labelNegative():
    with open("cascade/catch/neg.txt", "w") as f:
        for filename in os.listdir("cascade/catch/traningdata/neg"):
            f.write("cascade/catch/traningdata/neg/" + filename + "\n")

def takeScreenshots(fishing=False):
    scrw, scrh = pag.size()
    while True:
        inp = input("pics: ")
        interv = input("interval: ")
        time.sleep(5)
        for i in range(int(inp)):
            morigin = pag.position()
            pag.moveRel(random()*48-24,random()*48-24)

            mx, my = pag.position()
            #cast_dur = sqrt( pow( abs( scrw/2 -mx ), 2 ) + pow( abs( scrh/2 -my ), 2 ) - (scrw*0.1) ) / (scrw*0.33)
            now = datetime.datetime.now().microsecond

            if fishing:
                pag.mouseDown()
                time.sleep(0.5)
                pag.mouseUp()
                time.sleep(1)
                pag.click()
                time.sleep(.2)

            ss = pag.screenshot(region=(mx-64, my-64, 128, 128))
            ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGRA)
            cv2.imwrite("img/screenshot"+str(i)+str(now)+".png", ss)

            pag.moveTo(morigin[0],morigin[1])

            time.sleep(float(interv))
            print(str(i) + " " + str(now))
        print("done")

def screenPosPrinter():
    while True:
        xx, yy = pag.position()
        pos = (xx,yy)
        centx = pag.size()[0]/2
        centy = pag.size()[1]/2+270
        cent = (centx,centy)
        print(pointDistance(cent, pos))
        time.sleep(2)
