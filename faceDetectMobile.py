import requests
import numpy
import cv2
face=cv2.CascadeClassifier("/root/Desktop/haarcascade_frontalface_default.xml")

while True:
    url="http://25.110.108.26:8080/shot.jpg"
    data=requests.get(url)
    photo=data.content
    myphoto=bytearray(photo)
    my=numpy.array(myphoto)
    pic=cv2.imdecode(my,-1)   #-1 for converting into 3d array
    co=face.detectMultiScale(pic)
    if len(co)>=1:
        x1=co[0][0]
        x2=co[0][0]+co[0][2]
        y1=co[0][1]
        y2=co[0][1]+co[0][3]
        cv2.rectangle(pic,(x1,y1),(x2,y2),(255,255,255),1)
    cv2.imshow("hi",pic)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
print("total number of faces: {}".format(len(co)))
