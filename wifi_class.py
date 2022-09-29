import os
import time
from h11 import Request
import pyautogui as pag
import urllib3.request

class Wifi():
    test_url = 'http://google.com'

    def __init__(self, name):
        self.name = name
        self.backup = ""

    def test_wifi(self):  
        try:
            request = Request.get('http://google.com', timeout = 4)
            print("Connected to the Internet")
            return True
        except:
            print("No internet connection.")
            return False

    def connect_wifi(self):

        os.system(f'''cmd /c "netsh wlan connect name = {self.name}"''')  

home = Wifi("DuroFam")
#print(home.test_wifi())
#if home.test_wifi() == False:
 home.connect_wifi()

exit()
