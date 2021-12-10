# import os
# print(os.listdir())
# os.chdir('images')
# print(os.listdir())
# print(len(os.listdir()))

import cv2
import face_recognition as fr

# img = cv2.imread('test-set/4.jpg')

img = fr.load_image_file('test-set/7.jpg')
faces = fr.face_locations(img)

print(faces)
# count = 0
# for i in faces:
#     count += 1
#     cv2.imshow(f'{count}',i)
#     if cv2.waitKey(10000) or 0xFF==ord('q'):
#         cv2.destroyAllWindows()

for i in faces:
    (a,b,c,d) = i
    cv2.rectangle(img,(d-10,a-10),(b+10,c+10),(255,0,0),2)
    cv2.imshow("ssds",img)
    if cv2.waitKey(1000) or 0xFF==ord('q'):
        cv2.destroyAllWindows()