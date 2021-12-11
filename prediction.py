import cv2
import os
import numpy as np
import face_recognition as fr
from facerec import face_data_encodings
import time

dataset = os.listdir('images')
dataset = dataset[1:]
checked = [False]*len(dataset)
test_images = os.listdir('test-set')

def isthere(ret):        
    for i in range(len(ret)):
        if ret[i]:
            checked[i] = True
            print(dataset[i].split('.')[0])
            break
    return True

start = time.time()
for i in test_images:
    curr_image = cv2.imread(f'./test-set/{i}')
    faces = fr.face_locations(curr_image)
    print(len(faces))
    # faces = np.ndarray(faces)
    for face in faces:
        a,b,c,d = face
        frame = curr_image[a:c,d:b]
        curr_encoding = fr.face_encodings(frame)[0]
        # print(fr.face_encodings(frame))
        ret = fr.compare_faces(face_data_encodings, curr_encoding)
        print(ret)
        if isthere(ret):
            break

print(time.time()-start)




# d,a b,c heloloi