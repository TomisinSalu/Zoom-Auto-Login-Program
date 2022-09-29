import os
import pyautogui as pag
import time

bandicam = "C:\\Program Files\\Bandicam\\bdcam.exe"

def startRec():
    os.startfile(bandicam)
    time.sleep(1)
    pag.hotkey("fn", "F12")
    time.sleep(1)
    pag.hotkey("win", "down")
    
def endRec():
    os.startfile(bandicam)
    time.sleep(1)
    pag.hotkey("fn", "F12")

startRec()
#time.sleep(10)
#endRec()