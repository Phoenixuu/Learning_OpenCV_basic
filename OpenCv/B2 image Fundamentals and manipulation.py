import cv2 
import random

img = cv2.imread('computerVision.jpg',-1)

# print(img)
print(img.shape)
# print(type(img))

#Changing pixels color
# for i in range(100):
# 	for j in range(img.shape[1]):
# 		img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

# Copying & Pasting parts of Image
tag = img[300:400, 600:800]
img[200:300, 200:400] = tag 


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





