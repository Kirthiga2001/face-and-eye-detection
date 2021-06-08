import cv2

f=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
e=cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
'''i=cv2.imread("lena.jpg")

b=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

faces= f.detectMultiScale(b,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,0),3)


cv2.imshow("img",i)
cv2.waitKey(0)'''

cap=cv2.VideoCapture(0)

while 1:
    k,v=cap.read()
    faces = f.detectMultiScale(v, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(v, (x, y), (x + w, y + h), (0, 0, 0), 3)
    eye=e.detectMultiScale(v,1.1,4)
    for (x,y,w,h) in eye:
        cv2.circle(v,((x+w//2),(y+h//2)),2,(255,0,0),3)
    cv2.imshow("face",v)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


