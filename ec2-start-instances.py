# Script to start instances by using instance id directly.

import boto3
import json


def lambda_handler (event, context):

# To start the instances
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(
    InstanceIds=[
        'strings',
    ]
    )

# To stop the instances
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
    InstanceIds =[
        'strings'
        ]
    )
