import cv2
import face_recognition as fr
from facerec import face_data
from prediction import isthere

cam = cv2.VideoCapture(0)

while cam:
    _, img = cam.read()
    faces = fr.face_locations(img)
    cv2.imshow("Cam-1",cam)
    for face in faces:
        a,b,c,d = face
        frame = img[a:c,d:b]
        curr_encoding = fr.face_encodings(frame)[0]
        # print(fr.face_encodings(frame))
        ret = fr.compare_faces(face_data,curr_encoding)
        if isthere(ret):
            break

    if 0xFF==ord('q'):
        cv2.destroyAllWindows()