import cv2

#Gọi ảnh
# img = cv2.imread('computerVision.jpg', 1)
img = cv2.imread('opencv.png',-1)

#Thay đổi kích thước
img = cv2.resize(img, (400,400))
# img = cv2.resize(img, (0,0),fx=2,fy=2)

#xoay ảnh
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

#Tạo ảnh mới
# cv2.imwrite('new_img.jpg',img)


cv2.rectangle(img, (20,300), (30,300), (0,0,0), 5)


#Gọi ảnh, chạy chương trình
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
