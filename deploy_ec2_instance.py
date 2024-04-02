from boto3 import resource
import logging
from os import chmod

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def manage_ec2_resource():
    try:
        return resource('ec2', aws_access_key_id='your access_key', 
                        aws_secret_access_key='your secret_key', 
                        region_name='us-east-1')
    except Exception as e:
        logger.error(f"An error occurred while creating EC2 resource: {str(e)}")
        raise

def create_key_pairs(ec2_resource):
    try:
        key = ec2_resource.create_key_pair(KeyName='test_keypairboto1')
        with open('private-key.pem', 'w') as write_key:
            write_key.write(key.key_material)
        chmod('private-key.pem', 0o600)
        logger.info("Key pair created successfully.")
        return key.name
    except Exception as e:
        logger.error(f"An error occurred while creating key pair: {str(e)}")
        raise

def create_ec2_instance(ec2_resource, keypair):
    try:
        instance_payload = {
            'ImageId': 'ami-053b0d53c279acc90',
            'InstanceType': 't2.micro',
            'KeyName': f'{keypair}',
            'MinCount': 1,
            'MaxCount': 1,
            'TagSpecifications': [
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'boto-instance'
                        }
                    ]
                }
            ],
            'NetworkInterfaces': [
                {
                    'AssociatePublicIpAddress': True,
                    'DeviceIndex': 0,
                }
            ]
        }
        
        instances = ec2_resource.create_instances(**instance_payload)
        logger.info(f"Instance created successfully with ID: {instances[0].id}")
    except Exception as e:
        logger.error(f"An error occurred while creating EC2 instance: {str(e)}")
        raise

if __name__ == "__main__":
    ec2_resource = manage_ec2_resource()
    keypair = create_key_pairs(ec2_resource)
    create_ec2_instance(ec2_resource, keypair)
