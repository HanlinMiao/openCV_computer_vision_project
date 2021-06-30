import os
import cv2 as cv
import numpy as np

people = []
DIR = "/Users/hanlinmiao/Desktop/OpenCV/Faces/train"
haar_cascade = cv.CascadeClassifier("haar_face.xml")


for i in os.listdir(r"/Users/hanlinmiao/Desktop/OpenCV/Faces/train"):
    people.append(i)

# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(r"/Users/hanlinmiao/Desktop/OpenCV/Faces/val/elton_john/1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)

    print(f"label = {people[label]} with a confidence of {confidence}")

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, x+h), (0, 255, 0), thickness=2)

cv.imshow("Detected Face", img)

cv.waitKey(0)