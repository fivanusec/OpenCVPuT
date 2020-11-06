import os
import threading

class Camera:
    addr = ""
    port = 0

    def __init__(self):
        self.addr = input("Input camera IP address: ")
        self.port = input("Input camera port: ")

        camThread = threading.Thread(target=self.start, args=())
        camThread.start()

    def start(self):
        try:
            os.system(f"droidcam-cli {self.addr} {self.port}")
        except:
            print("There was an error with camera")
            
    