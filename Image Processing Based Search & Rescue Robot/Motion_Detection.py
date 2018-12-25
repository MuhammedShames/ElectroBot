import numpy as np
import cv2

cam=cv2.VideoCapture(0)

value = cv2.createBackgroundSubtractorMOG2()

while(1):
	ret,frame=cam.read()
	if frame is not None:
		mask=value.apply(frame)
		cv2.imshow('frame',mask)

		if cv2.waitKey(30) & 0xFF == 27:
			break
	else:
		break
cam.release()
cv2.destroyAllWindows()
