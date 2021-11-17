import sys
sys.path.append("../..")

import pyautogui as gui

from time import sleep
from random import random, choice
from botutils import findTempl, foundTempl, waitCountdown

class fisher():
    INITIALIZING, CASTING, WAITING, CATCH = 0, 1, 2, 3
    state = INITIALIZING

    def __init__():
        pass

    def goFishing():
        pos = (0,0)

        while True:
            if self.state == self.INITIALIZING:
                waitCountdown(5,1)
            if self.state == self.CASTING
                gui.press("f")
                w, h = gui.size()

                bobbers = findTempl("bobber", 0.9, (0,0,w,h))
                if len(bobbers) > 0:
                    x,y,w,h = bobbers[0]
                    pos = (x+w/2, y+h/2)
                    gui.moveTo(pos[0], pos[1], 0.5)
                    self.state = self.WAITING

            if self.state == self.WAITING
                findTempl("bobber_down", 0.8, (pos[]-64))
