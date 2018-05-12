# -*- coding: utf-8 -*-
import cv2
import sqlite3

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
#Local Binary Patterns Histograms
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognition/trainingUserData.yml")
 
def getProfile(id):
    conn=sqlite3.connect("FacesDB.db")
    cmd="SELECT * FROM People WHERE ID ="+str(id)
    cursor=conn.execute(cmd)
    profile=0
    for row in cursor:
        profile=row
    conn.close()
    return profile

font = cv2.FONT_HERSHEY_SIMPLEX
fontColor= (255,255,255)
while(True):
    ret, img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.35,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,255,255) ,2)
        id, conf=rec.predict(gray[y:y+h, x:x+w])
        print('UserID: '+str(id)+', Confidence: '+str(conf))
        profile=getProfile(id)
        if int(conf) < 75 or int(conf) > 100: profile=0
        if (profile!=0):
            cv2.putText(img, 'Name: ' +str(profile[1]), (x, y+h+30), font, 0.55, fontColor, 1)
            cv2.putText(img, 'Age: '+str(profile[2]), (x, y+h+60), font, 0.55, fontColor, 1)
            cv2.putText(img, 'Gender: '+str(profile[3]), (x, y+h+90), font, 0.55, fontColor, 1)
            cv2.putText(img, 'FaceID: '+str(profile[4]), (x, y+h+120), font, 0.55, fontColor, 1)
    cv2.imshow("Sample face detection", img)
    if (cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllwindows()
