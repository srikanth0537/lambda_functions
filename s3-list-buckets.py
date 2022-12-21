# To list existing buckets
import boto3
import json

def lambda_handler (event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print('Existing buckets:')
    print(response['Buckets'])

# To get the output with the names only

    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
