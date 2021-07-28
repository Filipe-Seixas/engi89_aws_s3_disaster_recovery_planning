import boto3

# Name of the service we want to connect to
s3 = boto3.resource('s3')

# Print out all buckets
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

