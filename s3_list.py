import logging
import boto3
from botocore.exceptions import ClientError
import os

s3_client = boto3.client('s3')
response = s3_client.list_objects(Bucket='chinmay-kt')

for r in response['Contents']:
    print(r['Key'])
print(response['Contents'])