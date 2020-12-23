import cv2
import face_recognition
import os

class Pictures:
    path = "Slike"
    images=[]
    classNames = []
    encondings = []
    returnList = []

    def __init__(self):
        self.importPictrues()
    
    def testImages(self, images, classNames, encodings):
        if(images == [] or classNames == [] or encodings == []):
            if(images == []):
                print("Images are empty!")
            elif(classNames == []):
                print("Classnames are empty")
            elif(encodings == []):
                print("Encodings are empty")
            else:
                print("Images loaded successfully!")

    def importPictrues(self):
        self.returnList.append(self.getPictures())
        self.returnList.append(self.getClassNames())
        self.returnList.append(self.getEncodings(self.images))
        return self.returnList

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
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            try:
                encode = face_recognition.face_encodings(img)[0]
                self.encondings.append(encode)
            except IndexError as err:
                print(f"Image error: {err}")

        return self.encondings