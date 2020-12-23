import os
import threading

class Camera:
    addr = ""
    port = 0

    def __init__(self):
        self.addr = input("Input camera IP address: ")
        self.port = input("Input camera port: ")

    def start(self):
        if len(self.addr) > 1 and len(self.port) > 1:
            camThread = threading.Thread(target=self.enableDroidCam, args=())
            camThread.start()
            return 0
        return 1

    def enableDroidCam(self):
        try:
            os.system(f"droidcam-cli {self.addr} {self.port}")
        except:
            print("There was an error with camera")