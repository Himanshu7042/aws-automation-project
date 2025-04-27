import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()

print("Available Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")

# Specify your bucket name
bucket_name = 'my-static-site-22025'

# Count objects in the specified bucket
object_list = s3.list_objects_v2(Bucket=bucket_name)

# Get the number of objects
num_objects = object_list.get('KeyCount', 0)

print(f"\nTotal objects in '{bucket_name}': {num_objects}")