# -*- coding: utf-8 -*-
import cv2
import sqlite3

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)

def insertOrUpdate(Id, Name):
	conn=sqlite3.connect("FacesDB.db")
	cmd="SELECT * FROM People WHERE ID="+str(Id)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if isRecordExist==1 :
		cmd="UPDATE People SET Name = '" +str(Name) + "' WHERE ID="+str(Id)
	else:
		cmd="INSERT INTO People(ID, Name) Values("+str(Id)+",'"+str(Name)+"')"
	conn.execute(cmd)
	conn.commit()
id=input("Введите ID человека : ")
name=input("Введите ФИО человека : ")
insertOrUpdate(id, name)

sampleNum=0

while(True):
	ret, img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.35,5)

	for(x,y,w,h) in faces:
		sampleNum=sampleNum+1
		cv2.imwrite("dataset_users/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
		cv2.rectangle(img, (x,y),(x+w,y+h),(255,255,255) ,2)
		cv2.waitKey(100)

	cv2.imshow("creatingDataset", img)
	cv2.waitKey(1)
	if sampleNum>100:
		print("Датасет создан!")
		break

cam.release()
cv2.destroyAllWindows() 
