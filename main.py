import cv2
import numpy as np
import face_recognition

# Moduels
from ImportPictures import Pictures
from Camera import Camera
from Process import Process
from Snapshot import Snapshot

# Declaration of pictures
pic = Pictures()

images = pic.returnList[0]
classNames = pic.returnList[1] 
encodings = pic.returnList[2]

# Test if images loaded correctly
pic.testImages(images,classNames,encodings)

# Init camera
camera = Camera()
device = camera.start()

print("Operating modes> \n")
print("1 for recognition")
print("2 for snapshot")
mode = int(input("Input the operating mode> "))
if(mode == 2):
    snapshot = Snapshot()
    snapshotPicture = snapshot.picture(device)
    save = snapshot.save(snapshotPicture)
    if(save):
        print("Snapshot saved!")
    else:
        print("Nothing was saved!")

else:
    cap = cv2.VideoCapture(device)
    # Intit Process
    process = Process(images, classNames, encodings, cap)