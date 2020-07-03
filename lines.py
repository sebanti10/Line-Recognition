import cv2
import numpy as np

img = cv2.imread('quiz.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,210,apertureSize = 3)
minLineLength = 150
maxLineGap = 20
lines = cv2.HoughLinesP(edges,1,np.pi/180,200,minLineLength,maxLineGap)
for line in lines:
	x1,y1,x2,y2 =line[0]
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('newlines.jpeg',img)