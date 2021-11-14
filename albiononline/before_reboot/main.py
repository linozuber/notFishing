import cv2
import numpy as np
import pyautogui as pag
import time

state = "initializing"
size = pag.size()
screenshots = []
templates = {}
casc_bobber_down = cv2.CascadeClassifier('cascade/cascade.xml')
#templ_data = [["bobber_dwn", 0.8, (0,0,255)]]
templ_data = {
    "bobber": ["bobber", 0.6, (255,0,0)],
    "bobber_down": ["bobber_down", 0.5, (0,255,0)],
    "bobber_left": ["bobber_left", 0.85, (255,255,255)],
    "bobber_right": ["bobber_right", 0.85, (255,255,255)],
    "bobber_bar": ["bobber_bar", 0.6, (255,255,255)],
    }

for td in templ_data:
    templates[td] = cv2.imread('img/tmpl/'+td+'.png', cv2.IMREAD_UNCHANGED)

def findTmpls(_tmpls, _loc=(0,0), _size=size ):
    ss = pag.screenshot(region=(_loc[0],_loc[1],_size[0],_size[1]))
    ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGRA)
    cv2.imwrite("img/screenshot.png", ss)
    ss = cv2.imread("img/screenshot.png", cv2.IMREAD_UNCHANGED)

    for tmplName in _tmpls:
        td = templ_data[tmplName]
        rectangles = []
        templ = templates[td[0]]
        result = cv2.matchTemplate(ss, templ, cv2.TM_CCOEFF_NORMED)
        ypos, xpos = np.where(result >= td[1])
        width = templ.shape[1]
        height = templ.shape[0]
        for (x, y) in zip(xpos,ypos):
            rectangles.append([x, y, width, height])
            rectangles.append([x, y, width, height])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.8)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(ss, (x, y), (x+w, y+h), td[2], 2)

    if len(rectangles) > 0:
        cv2.imshow('Game', ss)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

    return rectangles

def findTmplsCasc(_tmpls, _loc=(0,0), _size=size ):
    ss = pag.screenshot(region=(_loc[0],_loc[1],_size[0],_size[1]))
    ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGRA)
    cv2.imwrite("img/screenshot.png", ss)
    ss = cv2.imread("img/screenshot.png", cv2.IMREAD_UNCHANGED)

    for tmplName in _tmpls:
        td = templ_data[tmplName]

    rectangles = []
    rectangles = casc_bobber_down.detectMultiScale(ss)

    if len(rectangles) > 0:
        for (x, y, w, h) in rectangles:
            cv2.rectangle(ss, (x, y), (x+w, y+h), td[2], 2)

        cv2.imshow('Game', ss)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

    return rectangles

#for ss in screenshots

while True:
    mx, my = pag.position()

    if state == "initializing":
        print(3)
        time.sleep(1)
        #print(2)
        #time.sleep(1)
        #print(1)
        #time.sleep(1)

        print("init cast")
        time.sleep(1)
        if len(findTmpls(["bobber"])) > 0:
            print("init position mouse")
            time.sleep(1)

            print("state > casting")
            state = "casting"

        print("init click to recall bobber")

    if state == "casting":
        print("init cast")

        print("state > waiting")
        state = "waiting"

    if state == "waiting":
        if len(findTmplsCasc(["bobber_down"], (mx-64,my-64), (128,128))):
            print("recall bobber")

            print("state > thrill")
            state = "thrill"

    if state == "thrill":
        if len(findTmpls(["bobber_right"], (size[0]/2-256,size[1]/2-32), (512,64))):
            print("let go")

            print("state > letloose")
            state = "letloose"

    if state == "letloose":
        if len(findTmpls(["bobber_left"], (size[0]/2-256,size[1]/2-32), (512,64))):
            print("pull")

            print("state > thrill")
            state = "thrill"

    if state == "letloose" or state == "thrill":
        if len(findTmpls(["bobber_bar"], (size[0]/2-256,size[1]/2-32), (512,64))) < 1:
            print("done/failed")

            print("state > cast")
            state = "waiting"
