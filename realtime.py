import cv2
import numpy as np
import face_recognition as fr
from facerec import face_data_encodings,names
from prediction import isthere
from datetime import datetime
import  time


cam = cv2.VideoCapture(0)
presenties = []
ptime=[]


def markAttendance(matches,matcheindex):
    if matches[matchindex]:
        name = names[matchindex].upper()
        if name not in presenties:
            presenties.append(name)
            now = datetime.now()
            ptime.append(now.strftime('%H:%M:%S'))
    print(presenties)
    print(ptime)



while True:
    success, img = cam.read()


    capturedfaces = fr.face_locations(img)
    capturedFacesEncodings = fr.face_encodings(img,capturedfaces)


    for faces,faceEncode in zip(capturedfaces,capturedFacesEncodings):
        matches = fr.compare_faces(face_data_encodings,faceEncode)
        faceDistance = fr.face_distance(face_data_encodings,faceEncode)

        matchindex = np.argmin(faceDistance)


        markAttendance(matches,matchindex)


        """if matches[matchindex]:
            name = names[matchindex].upper()
            if name not in presenties:
                presenties.append(name)
                now = datetime.now()
                ptime.append(now.strftime('%H:%M:%S'))

    print(presenties)
    print(ptime)"""
    noOfstudentsPresent = len(presenties)
    cv2.imshow("cmaOn", img)
    cv2.waitKey(1)
    time.sleep(3)














"""while True:
    _, img = cam.read()
    faces = fr.face_locations(img)
    
    cv2.imshow("Cam-1",img)
    for face in faces:
        a,b,c,d = face
        frame = img[a:c,d:b]
        curr_encoding = fr.face_encodings(frame)[0]
        # print(fr.face_encodings(frame))
        ret = fr.compare_faces(face_data_encodings, curr_encoding)
        if isthere(ret):
            break

    if 0xFF==ord('q'):
        cv2.destroyAllWindows()"""