import cv2

class Snapshot:
    def picture(self, device):
        webcam = cv2.VideoCapture(device)
        check, frame = webcam.read()
        if check:
            cv2.namedWindow("Snapshot")
            cv2.imshow("Snapshot",frame)
            cv2.waitKey(0)
            cv2.destroyWindow("Snapshot")
        return frame
            
    def save(self, frame):
        confirmation = str(input('Are you satisfied with your picture?(y/n)> '))
        while(confirmation!= 'y' or confirmation !='n'):
            if confirmation == 'y':
                ime = input("Input snapshot name> ")
                cv2.imwrite("Slike/{}.jpg".format(ime), frame)
                return True
            elif confirmation == 'n':
                break
            print("Invalid input!> ")
            confirmation = str(input('Are you satisfied with your picture?(y/n)> '))

        return False
        