import os
import cv2 
# import face_recognition as fr


cam = cv2.VideoCapture(0)
images = []

no_of_images = len(os.listdir('./images'))
print(no_of_images)

# images.append(fr.load_image_file('./images/charan'))