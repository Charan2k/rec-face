import boto3
import cv2
from vars import folder_name, bucket_name

# img = cv2.imread(f'{folder_name}/501.jpeg')
s3 = boto3.client('s3')
# file_name = '501.jpeg'

def uploadToS3(file_name):
    with open(f'{folder_name}/{file_name}', 'rb') as data:
        s3.upload_fileobj(data, bucket_name, f'{folder_name}/504.jpeg')

uploadToS3('501.jpeg')