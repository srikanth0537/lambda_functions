import json
import boto3
import os

# region = os.environ['REGION']
# instance_type = os.environ['INSTANCE_TYPE']
# image_id = os.environ['IMAGE_ID']
InstanceId = os.environ['INSTANCE_ID']
instance_type = os.environ['INSTANCE_TYPE']

### Function-1
# To stop the instance
ec2 = boto3.client('ec2')
response = ec2.stop_instances(InstanceIds=[InstanceId])

# wait for the instance to be in the stopping state
ec2.get_waiter('instance_stopped').wait(InstanceIds=[InstanceId])

def lambda_handler(event, context):
    # TODO implement
    
### Function-2
    ec2 = boto3.client('ec2')
    response = ec2.modify_instance_attribute(
        InstanceId=InstanceId,
        Attribute='instanceType',
        Value=instance_type
        )
        
    print(response)
