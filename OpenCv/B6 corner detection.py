import numpy as np 
import cv2

img = cv2.imread('chess.png')
img = cv2.resize(img, (0,0), fx=2, fy=2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# goodFeaturesToTrack(source image, number of corners, minimun quality, minimum euclidean distance)
# euclidean distance
# (x1, y1) (x2,y2)
# sqrt((x2-x1)^2 + (y2 - y1)^2)

corners = np.int0(corners)

#detect corner
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

#draw line
for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()