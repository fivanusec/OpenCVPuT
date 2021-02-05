import cv2
import face_recognition
import threading
import numpy as np
from Filewrite import Writer

class Process:

    def __init__(self, images, classNames, encodings, cap):
        recognitionThread = threading.Thread(target=self.recognition, args=(images, classNames, encodings, cap))
        recognitionThread.start()
        if recognitionThread == True:
            recognitionThread._stop()
    
    def recognition(self,images, classNames, encodings, cap):
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurrFrame = face_recognition.face_locations(imgS)
            encodesCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

            for encodeFace, faceloc in zip(encodesCurrFrame, facesCurrFrame):
                matches = face_recognition.compare_faces(encodings, encodeFace)
                faceDis = face_recognition.face_distance(encodings, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    print(name)
                    y1,x1,y2,x2 = faceloc
                    y1,x1,y2,x2 = y1*4,x1*4,y2*4,x2*4 
                    cv2.rectangle(img, (x1,y1), (x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0), cv2.FILLED)
                    cv2.putText(img, name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0),2)
                    writer = Writer()
                    writer.wirte(name) 
                    return True
                else:
                    print("No match")
                    y1,x1,y2,x2 = faceloc
                    y1,x1,y2,x2 = y1*4,x1*4,y2*4,x2*4 
                    cv2.rectangle(img, (x1,y1), (x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0), cv2.FILLED)
                    cv2.putText(img, "No match",(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0),2)
            
            cv2.imshow('Webcam', img)
            cv2.waitKey(1)