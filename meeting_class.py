import os
import time
import pyautogui as pag
import schedule

class Meeting():
    myName = "Tomisin Salu"
    zoom = "C:\\Users\\Tomi Salu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    bandicam = "C:\\Program Files\\Bandicam\\bdcam.exe"
    def __init__(self, name, ID, passcode, start_time, end_time):
        self.name = name
        self.ID = ID
        self.passcode = passcode
        self.start_time = "8:00"
        self.end_time = "12:48"

    def join_meeting(self):
        os.startfile(self.zoom)

        time.sleep(2)

        pag.hotkey("win", "up")
        x, y = pag.locateCenterOnScreen("C:\\Python\\zoom_join.png", confidence = 0.9)
        pag.moveTo(x, y)
        pag.click()

        time.sleep(1)

        pag.write(self.ID)
        pag.press("tab")
        pag.press("tab")


        pag.hotkey("ctrl", "a")
        pag.press("delete")
        pag.write(self.myName)

        x, y = pag.locateCenterOnScreen("C:\\Python\\join_meeting.png", confidence= 0.9)
        pag.moveTo(x, y)
        pag.click()

        time.sleep(4)

        if (pag.locateCenterOnScreen("C:\\Python\\passcode_indicator.png", confidence= 0.9) != None) :
            pag.write(self.passcode) #Enter meeting passcode
            pag.press("enter") 
        else:
            time.sleep(3)
        """    
        time.sleep(4)

        if (pag.locateCenterOnScreen("C:\\Python\\muted_mic.png", confidence= 0.95) == None):
            pag.hotkey("alt", "m") #mute microphone
        else:
            pass

        if (pag.locateCenterOnScreen("C:\\Python\\joined_indicator.png", confidence= 0.9) != None):
            pag.hotkey("win", "up") #Maximise window
        """

    def leave_meeting(self):
        #x, y = pag.locateCenterOnScreen("C:\\Python\\zoom_join.png", confidence = 0.9)
        pag.moveTo(1920, 10)
        pag.doubleClick()
        pag.moveTo(950, 800)
        #pag.pess("enter")

    def startRec(self):
        os.startfile(self.bandicam)
        time.sleep(2)
        pag.hotkey("fn", "F12")
        time.sleep(2)
        pag.hotkey("win", "down")
        
    def endRec(self):
        os.startfile(self.bandicam)
        time.sleep(1)
        pag.hotkey("fn", "F12")


french = Meeting("French", "2063523039", "570581", "14:05", "18:00")
#french.join_meeting()
#time.sleep(10)
#french.startRec()
#time.sleep(3)
#french.leave_meeting()

schedule.every().day.at("14:06").do(french.join_meeting)
#schedule.every().day.at("12:47").do(french.startRec)
#schedule.every().day.at(french.end_time).do(french.leave_meeting)
#schedule.every().day.at("12:50").do(french.endRec)


while True:
    schedule.run_pending()
    time.sleep(1)