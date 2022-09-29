import os
import pyautogui as pag
import time

#Make into instance of meeting class
meetingName = "French"
name = "Tomisin Salu"
meetingID = "5723331075"
passcode = "skUbQ1"
startTime = "9:00am"
endTime = "1:00pm"

#Open zoom application
def joinMeeting():
    zoom = "C:\\Users\\Tomi Salu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    os.startfile(zoom)

    time.sleep(2)

    pag.hotkey("win", "up")
    x, y = pag.locateCenterOnScreen("C:\\Python\\zoom_join.png", confidence = 0.9)
    pag.moveTo(x, y)
    pag.click()

    time.sleep(1)

    pag.write(meetingID)
    pag.press("tab")
    pag.press("tab")


    pag.hotkey("ctrl", "a")
    pag.press("delete")
    pag.write(name)

    x, y = pag.locateCenterOnScreen("C:\\Python\\join_meeting.png", confidence= 0.9)
    pag.moveTo(x, y)
    pag.click()

    time.sleep(10)

    if (pag.locateCenterOnScreen("C:\\Python\\join_meeting.png", confidence= 0.9) == None):
        pag.write(passcode)
        pag.press("enter") 

    time.sleep(15)
    pag.hotkey("win", "up") #Maximise window

def startRec():
    pag.hotkey("win", "alt", "r")

joinMeeting()
time.sleep(14)
startRec()
