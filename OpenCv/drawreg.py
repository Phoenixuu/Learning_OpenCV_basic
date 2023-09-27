import cv2
import time

img = cv2.imread("blackimg.jpg",-1)


img = cv2.resize(img, (640,480))
 
cv2.line(img, (0,480), (640,0), (255,255,255), 1)

# for x in range(20,640,20):
# 	for y in range(15,480,15):
# 		cv2.rectangle(img, (x,480-y), (x*2,480-y*2), (255,255,255), -1)

# cv2.imshow('Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from decimal import Decimal


def lin_equ(l1, l2):
    """Line encoded as l=(x,y)."""
    m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
    c = (l2[1] - (m * l2[0]))
    return m, c

m, c = lin_equ((0, 480), (640, 0))
print(m, c)
for x in range(0, 640, 25):
	y = int(m * x + c)
	cv2.rectangle(img, (x, y), (x+20, y+15), (255,255,255), 2)
	# cv2.rectangle(img, (x, y), (x+12, y+8), (255,255,255), 1)
	# time.sleep(0.5)
	
	cv2.imshow('Image',img)
	# print(t)
	cv2.waitKey(0)
	cv2.destroyAllWindows() 


