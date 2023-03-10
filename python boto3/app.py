from dotenv import load_dotenv
import os
import boto3

# Load environment variables
load_dotenv()
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Create an S3 client object
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

bucket_name='bucker-name-123'
# # s3 = boto3.client('s3')
key="suriya.png"
# with open("suriya.png", "rb") as f:
#     s3.upload_fileobj(f, bucket_name, key)

expiration=600
#key is the path

url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': key},
    ExpiresIn=expiration
)

print(url)