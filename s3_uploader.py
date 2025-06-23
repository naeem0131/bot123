import boto3
import os

# ✅ Make sure this region matches your S3 bucket region
s3 = boto3.client('s3', region_name='eu-north-1')

bucket_name = 'bot123-backup'
local_file_path = "C:/Users/Naeem/Downloads/patch1.zip"
s3_key = "bot123/patch1.zip"

s3.upload_file(local_file_path, bucket_name, s3_key)
print("✅ Upload successful!")
