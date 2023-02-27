import cv2 
img = cv2.imread("butterfly.jpg")
cv2.imshow("displayImage",img)
grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("GrayScaleImage",grayimg)
print(img)
cv2.waitKey(0)