import cv2
import random

random.seed(version=2)
uniqueFaces = []  
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
face_id = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor= 1.05,
        minNeighbors= 5,
        minSize=(20, 20)
    )
    
    for (x, y, w, h) in faces:

        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 0), 2)
        if not uniqueFaces:
            uniqueFaces.append([x,y+h,face_id])    
        for (x2,y2,face_id) in uniqueFaces: # если появляется новое лицо он начинает бесконечно добавлять лица
            if (abs(x-x2) < 70 & abs(y-y2) < 70):
                x2 = x
                y2 = y
            else:
                face_id+=1
                uniqueFaces.append([x,y+h,face_id])      #contain face coordinates and id
                break
        
    for (face) in uniqueFaces:
        cv2.putText(gray, str(face[2]), (face[0],face[1]),1, 3, (255, 255, 255), 2)

     #Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

def showimage (image,size):
    width = int(image.shape[1] * size / 100)
    height = int(image.shape[0] * size / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Output",image)
    cv2.waitKey(0)
