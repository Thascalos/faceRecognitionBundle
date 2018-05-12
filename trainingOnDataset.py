# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image

#Local Binary Patterns Histograms
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset_users'

def getImagesWithID(path):
    faces=[]
    IDs=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)

    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg, 'uint8')
        ID=int(os.path.split(imagePath) [-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Learning in progress", faceNp)
        cv2.waitKey(50)
    return np.array(IDs), faces

IDs, faces= getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.write('recognition/trainingUserData.yml')
cv2.destroyAllWindows()
print ("Обучение завершено. Теперь можно тестировать распознавание лиц.")
