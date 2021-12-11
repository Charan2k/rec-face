import boto3
import cv2
from vars import *


s3 = boto3.resource('s3', region_name='us-east-2')
bucket = s3.Bucket(bucket_name)

def download(filename):
    object = bucket.Object(f'{folder_name}/{filename}')
    object.download_file(f'{folder_name}/{filename}')
    img=cv2.imread(f'{folder_name}/{filename}')
    print(img)
    cv2.imshow("kya bolti publix",img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


def get_filenames():
    files_in_s3 = [f.key.split(folder_name + "/")[1] for f in bucket.objects.filter(Prefix=folder_name).all()]
    files_in_s3 = files_in_s3[1:]
    for filename in files_in_s3:
        download(filename)

get_filenames()