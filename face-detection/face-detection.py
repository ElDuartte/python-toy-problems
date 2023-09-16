import cv2

face_casade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# add your img
img = cv2.imread("test1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_casade.detectMultiScale(gray, 1.1, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 10)

cv2.imshow("img", img)
cv2.waitKey()

cv2.imwrite("face_detected.jpg", img)
