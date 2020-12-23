import cv2
import numpy as np
import face_recognition

# Moduels
from ImportPictures import Pictures
from Camera import Camera
from Process import Process

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

cap = cv2.VideoCapture(device)

# Intit Process
process = Process(images, classNames, encodings, cap)