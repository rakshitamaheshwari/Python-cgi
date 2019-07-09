import cv2
cap=cv2.VideoCapture(0)
while True:
	ret,pic=cap.read()
	cv2.imshow('rakshita',pic)
	if cv2.waitKey(1)==13:
		break
cv2.destroyAllWindows()
cap.release()
