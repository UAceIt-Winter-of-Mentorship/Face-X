import cv2

img_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('abc.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = img_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
