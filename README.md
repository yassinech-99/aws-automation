# aws-automation
### AWS Automation Repository (aws-auto)

This repository contains scripts to automate the creation of an EC2 instance on AWS using both Python with Boto3 and Ansible. The goal is to demonstrate how you can use these tools together to streamline the process of deploying resources on AWS.

#### Scripts Included:

1. **deploy_ec2_instance.yaml**:
   - This Ansible playbook (`deploy_ec2_instance.yaml`) is designed to create an EC2 instance on AWS.
   - It performs the following tasks:
     - Creates an EC2 key pair named "test_keypair_ansible".
     - Saves the private key to a local file `private-key.pem` with the correct permissions.
     - Launches an EC2 instance with the specified configuration.

2. **deploy_ec2_instance.py**:
   - This Python script (`deploy_ec2_instance.py`) uses Boto3, the AWS SDK for Python, to achieve similar functionality to the Ansible playbook.
   - It provides the following functions:
     - `manage_ec2_resource()`: Creates an EC2 resource using Boto3.
     - `create_key_pairs(ec2_resource)`: Creates an EC2 key pair named "test_keypair_python" and saves the private key to a local file.
     - `create_ec2_instance(ec2_resource, keypair)`: Launches an EC2 instance with the specified configuration.

#### Requirements:
- Python 3.x installed on your system.
- Boto3 library installed (`pip install boto3`).
- Ansible installed on your system if you wish to use the Ansible playbook (`pip install ansible`).

#### Usage:

1. **Using the Python Script (`deploy_ec2_instance.py`)**:
   - Before running the script, make sure to set your AWS Access Key ID and Secret Access Key in the script.
   - Execute the script:
     ```bash
     python deploy_ec2_instance.py
     ```
   - This will create an EC2 instance on your AWS account with the specified configuration.

2. **Using the Ansible Playbook (`deploy_ec2_instance.yaml`)**:
   - Before running the playbook, ensure you have Ansible installed and configured.
   - Edit the `deploy_ec2_instance.yaml` file to set your AWS Access Key ID and Secret Access Key.
   - Execute the playbook:
     ```bash
     ansible-playbook deploy_ec2_instance.yaml
     ```
   - This will create an EC2 instance on your AWS account using Ansible.

#### Notes:
- **AWS Credentials**:
  - It's recommended to use AWS IAM roles or securely manage your AWS Access Key ID and Secret Access Key.
- **EC2 Instance Configuration**:
  - Both scripts are set to launch a t2.micro instance with an Ubuntu Server AMI (`ami-053b0d53c279acc90`) in the `us-east-1` region.
  - You can modify the `InstanceType`, `ImageId`, `KeyName`, and other parameters as needed for your use case.


