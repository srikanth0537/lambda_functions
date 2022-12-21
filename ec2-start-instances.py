# Script to start instances by using instance id directly.

import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler (event, context):

    response = ec2.start_instances(
    InstanceIds=[
        'strings',
    ]
    )
