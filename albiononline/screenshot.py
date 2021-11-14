import cv2
import numpy as np
import pyautogui as pag
import time
import datetime
from math import sqrt

scrw, scrh = pag.size()

while True:
    inp = input("pics: ")
    interv = input("interval: ")
    time.sleep(5)
    for i in range(int(inp)):
        mx, my = pag.position()
        #cast_dur = sqrt( pow( abs( scrw/2 -mx ), 2 ) + pow( abs( scrh/2 -my ), 2 ) - (scrw*0.1) ) / (scrw*0.33)
        now = datetime.datetime.now().microsecond

        pag.mouseDown()
        time.sleep(0.8)
        pag.mouseUp()
        time.sleep(1)
        pag.click()
        time.sleep(.2)
        ss = pag.screenshot(region=(mx-64, my-64, 128, 128))
        ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGRA)
        cv2.imwrite("img/screenshot"+str(i)+str(now)+".png", ss)

        time.sleep(float(interv))
        print(str(i) + " " + str(now))
    print("done")
