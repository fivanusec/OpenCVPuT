import cv2
import face_recognition
import os

class Pictures:
    path = "Slike"
    images=[]
    classNames = []

    def getPictures(self):
        dirList=os.listdir(self.path)

        for data in dirList:
            currImg = cv2.imread(f"{self.path}/{data}")
            self.images.append(currImg)
        return self.images

    def getClassNames(self):
        dirList = os.listdir(self.path)

        for data in dirList:
            self.classNames.append(os.path.splitext(data)[0])
        return self.classNames

    def getEncodings(self,images):
        encondings = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encondings.append(encode)
        
        return encondings