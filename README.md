# AWS S3 Disaster Recovery Plan

<p align="center">
<img src=s3_diagram.PNG>
</p>

## Setting up S3 on an EC2 instance

- Update and install python3 and pip3
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python3
sudo apt-get install python3-pip -y
```

- Install awscli with python3
`sudo python3 -m pip install awscli` or `sudo pip3 install awscli`

- Configure aws with excel details `aws configure`
	1. Access Key ID
	2. Secret Access Key
	3. Default region name: eu-west-1
	4. Default output format: json


```bash
# List all buckets 
aws s3 ls
# Make an s3 bucket 
aws s3 mb s3://eng89filipe --region eu-west-1
# Create txt file 
sudo nano test.txt
# Copy a file to bucket 
aws s3 cp test.txt s3://eng89filipe/
# Delete file from ec2 
rm -rf test.txt
# Download a file from s3 bucket 
aws s3 cp s3://eng89filipe/test.txt test1.txt
# Delete file from s3 bucket 
aws s3 rm s3://eng89filipe/test.txt
# Remove s3 bucket 
aws s3 rb s3://eng89filipe
```


### TROUBLESHOOTING PYTHON3
```bash
#check python3 is installed
python3 --version

#install awscli with python3
python3 -m pip install awscli

-- OR --

#create an alias for python3
alias python = python3

#install awscli with python3
python -m pip install awscli
```

## BOTO3 TASK

- Create new instance ec2
- SSH into it

### Installing python3.9
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
apt list | grep python3.9
sudo apt-get install python3.9
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --config python3
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
alias python=python3
```

- Install boto3 with pip `python -m pip install boto3`

- Install awscli `python -m pip install awscli`

- Configure aws with excel details `aws configure`
	- Access Key ID
	- Secret Access Key
	- Default region name: eu-west-1
	- Default output format: json

- List all buckets `aws s3 ls`

### Using boto3 in python script to manage s3
```bash
import boto3

# Name of the service we want to connect to
s3 = boto3.client('s3')

# Print out all bucket names
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Create new bucket
s3.create_bucket(Bucket='eng89-filipe-boto3', CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-1'})

# Upload a new file
s3.upload_file('test1.txt', 'eng89-filipe-boto3', 'test1.txt')

# Downloading a file
s3.download_file('eng89-filipe-boto3', 'test1.txt', 'test2.txt')

# Delete a file
s3.delete_object(Bucket='eng89-filipe-boto3', Key='test1.txt')

# Delete a bucket
s3.delete_bucket(Bucket='eng89-filipe-boto3')
``` 
- S3 functions: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object