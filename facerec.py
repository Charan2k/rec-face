import os
import cv2 
import face_recognition as fr


# cam = cv2.VideoCapture(0)
images = []

image_files = os.listdir('images')
image_files = image_files[1:]

# images.append(fr.load_image_file('./images/charan.png'))
# print(images[0])
names = []
for i in image_files:
    img = cv2.imread(f'./images/{i}')
    images.append(img)
    names.append(i.split('.')[0])
    # print(names)

count = 0
# for i in images:
#     count += 1
#     cv2.imshow(f'{count}',i)
#     if cv2.waitKey(1000) or 0xFF==ord('q'):
#         cv2.destroyAllWindows()


def DbEncodings(images):
    encList = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        enc = fr.face_encodings(image)[0]
        # print(enc)
        encList.append(enc)
    return encList

face_data = DbEncodings(images)

# test_images = os.listdir('test-set')
# for i in test_images:
#     curr_image = cv2.imread(f'./test-set/{i}')
#     curr_encoding = fr.face_encodings(curr_image)[0]
#     ret = fr.compare_faces(face_data,curr_encoding)
#     print(ret)


# curr_image = cv2.imread('./test-set/predict_image.jpg')
# curr_encoding = fr.face_encodings(curr_image)[0]
# ret = fr.compare_faces(face_data,curr_encoding)
# print(ret)