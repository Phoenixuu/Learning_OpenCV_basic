import numpy as np 
import cv2

img = cv2.imread('book1.jpg',0)
img = cv2.resize(img, (400,400))
template = cv2.imread('sach.jpg',0)
template = cv2.resize(template, (50,50))
h,w = template.shape
# (height, width, channels)

#Template matching method
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
			cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
	img2 = img.copy()

#Displaying matches
	result = cv2.matchTemplate(img2, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	print(min_loc, max_loc)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_loc
	else:
		location = max_loc

	bottom_right = (location[0] + w, location[1] + h)	
	cv2.rectangle(img2, location, bottom_right, 255,5)
	cv2.imshow('Mactch',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


