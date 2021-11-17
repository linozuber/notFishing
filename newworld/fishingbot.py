import sys
sys.path.append("../")

import pyautogui as gui
from time import sleep
from random import random, choice
from botutils import findTempl, foundTempl, waitCountdown


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
        cent = (size[0]/2, size[1]/2)

        while True:
            if self.state == self.INITIALIZE:
                waitCountdown(5,1)
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
                if foundTempl("casting", 0.7 ,(xx,yy,ww,hh)):
                    gui.mouseUp()
                    self.state = self.CASTING
