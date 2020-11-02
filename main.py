import cv2
import numpy as np
import face_recognition
from ImportPictures import Pictures

"""
Jednostavni program za usporedbu lica 
"""
"""
imgFilip = face_recognition.load_image_file('Slike/Test3.jpg')
imgFilip = cv2.cvtColor(imgFilip,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Slike/Test4.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgFilip)[0]
encodeFilip = face_recognition.face_encodings(imgFilip)[0]
cv2.rectangle(imgFilip,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeFilip],encodeTest)
faceDis = face_recognition.face_distance([encodeFilip], encodeTest)

print(results, faceDis)

cv2.imshow("Filip", imgFilip)
cv2.imshow("Test", imgTest)
cv2.waitKey(0)

Prikaz
cv2.imshow('Filip', imgFilip)
cv2.imshow('Test', imgTest)
cv2.waitKey(0)
"""

images = []
classNames = [] 
encodings = []
pic = Pictures()

images = pic.getPictures()
classNames = pic.getClassNames()
encodings = pic.getEncodings(images)

if(images == [] or classNames == [] or encodings == []):
    if(images == []):
        print("Images are empty!")
    elif(classNames == []):
        print("Classnames are empty")
    elif(encodings == []):
        print("Encodings are empty")
else:
    print("Images loaded successfully!")