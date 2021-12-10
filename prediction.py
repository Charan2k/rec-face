import cv2
import os
import numpy as np
import face_recognition as fr
from facerec import face_data
import time


test_images = os.listdir('test-set')

start = time.time()
for i in test_images:
    curr_image = cv2.imread(f'./test-set/{i}')
    faces = fr.face_locations(curr_image)
    # faces = np.ndarray(faces)
    for face in faces:
        a,b,c,d = face
        frame = curr_image[a:c,d:b]
        curr_encoding = fr.face_encodings(frame)[0]
        # print(fr.face_encodings(frame))
        ret = fr.compare_faces(face_data,curr_encoding)
        print(ret)
print(time.time()-start)




# d,a b,c