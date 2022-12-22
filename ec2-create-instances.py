import json
import boto3
import os

region = os.environ['REGION']
instance_type = os.environ['INSTANCE_TYPE']
image_id = os.environ['IMAGE_ID']

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MaxCount=1,
        MinCount=1
        )

    print(response)
