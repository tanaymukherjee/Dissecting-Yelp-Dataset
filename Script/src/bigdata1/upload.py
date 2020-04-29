#!/usr/bin/python

import os
import sys
import boto3

# get an access token, local (from) directory, and S3 (to) directory
# from the command-line
local_directory, bucket, destination = sys.argv[1:4]

# Call the necessary boto3 function with the 's3' argument to initiate the AWS connection
client = boto3.client('s3')

# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    # construct the full Dropbox path
    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = os.path.join(destination, relative_path)

    try:
        client.head_object(Bucket=bucket, Key=s3_path)

    except:
        client.upload_file(local_path, bucket, s3_path)