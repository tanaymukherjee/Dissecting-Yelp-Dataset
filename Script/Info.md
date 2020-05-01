# Automating data upload directly into S3 using Kaggle APIs

## Additional Exercise
*This is an extra credit exercise for this project.*

## Objective:
To write a python or bash script that leverages the kaggle API module to download the dataset and the AWS boto3 module to upload to S3. This script must run in a docker container and it should work for anyone’s AWS and Kaggle accounts for any dataset. (For example, if I wanted to download kaggle dataset ABC and then upload it to my S3 bucket DEF - I should be able to manage this. This script must not be specific to the datasets or accounts for this project).

### A) File Structure
![s3_tree](https://user-images.githubusercontent.com/6689256/80568817-b7985d80-89c5-11ea-8da1-090745e058b9.PNG)

### B) Associated Files

* ```main.py```
``` 
It parses the arguments --data_url, --file_name into the download.py file for function call.
The code can be found in this repository under 'Script' folder.
```

* ```downlaod.py```
``` 
It has all the functions and error handling code to implement the exercise. 
The APP Id, APP Token, Domain, etc are also defined here alongside necessary packages.
The code can be found in this repository under Script > src > bigdata1
```

* ```uplaod.py```
``` 
It has all the functions and arguments to call the file name and path from local machine and pass it on to AWS S3. 
The original files path, bucket's name and the s3 path.
The code can be found in this repository under Script > src > bigdata1
```

#### 2. Supplementary Files:
* ```Docker File```
``` 
It is a text document that contains all commands a user could call on the command line to assemble an image.
It is located in the root directory of our project.
```

* ```Requirements.txt```
``` 
This file is used for specifying what python packages are required to run the project you are looking at.
It is located in the root directory of our project.
```

### C) Commands

#### 1. Docker Build:
* ```Docker build```
``` 
docker build -t bigdata1:3.0 .
```
* ```Docker run on /bin/bash```
```
docker run -v "$(pwd):/app" -e KAGGLE_USERNAME = <username> KAGGLE_TOKEN = <api_token> -it bigdata1:3.0 /bin/bash
```
* ```Docker mount with arguments```
```
docker run -v "$(pwd):/app" -e KAGGLE_USERNAME = <username> KAGGLE_TOKEN = <api_token> -it bigdata1:3.0 python -m main ----data_url = <URL for kaggel dataset> --file_name = <name of the file to be saved>
```

#### 2. Setup AWS API:
First, install the AWS Software Development Kit (SDK) package for python: boto3. boto3 contains a wide variety of AWS tools, including an S3 API, which we will be using.

To use the AWS API, you must have an AWS Access Key ID and an AWS Secret Access Key (doc). It would also be good to install the AWS Command Line Interface (CLI) as it is the AWS API in the terminal.

Now you must set up your security credentials. If you have AWS CLI installed, simply run aws configure and follow the instructions. Else, create a file ~/.aws/credentials with the following:
```
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

**NOTE:** There are two main tools you can use to access S3: clients and resources. Clients are low-level functional interfaces, while resources are high-level object-oriented interfaces. I typically use clients to load single files and bucket resources to iterate over all items in a bucket.

#### 3. Deployment:
* ```For initiating it via Python```
```
import boto3

client = boto3.client('s3') #low-level functional API
resource = boto3.resource('s3') #high-level object-oriented API
my_bucket = resource.Bucket('my-bucket') #subsitute this for your s3 bucket name.
```

* ```Uploading the file```
```
upload.py </path/to/local/folder> <s3 bucket name> </path/to/s3/folder>
```

## Appendix
### A) References

#### 1. Guide
* ```Prof. Taqqui Karim```
``` 
Subject: 9760 - Big Data Technologies
Session: Spring, 2020
```

#### 2. Links
- [Accessing S3 Data in Python with boto3](https://dluo.me/s3databoto3)
- [Uploading files on Amazon S3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
- [How to use Kaggle API](https://github.com/Kaggle/kaggle-api)

#### 3. Additional Reading
- [AWS Lambda and boto3](https://towardsdatascience.com/introduction-to-amazon-lambda-layers-and-boto3-using-python3-39bd390add17)
- [Bash script to upload folder to S3](https://gist.github.com/ryantbrown/b643f678f174013ae92e488850ce699f)
- [Streaming Data to Amazon S3](https://towardsdatascience.com/delivering-real-time-streaming-data-to-amazon-s3-using-amazon-kinesis-data-firehose-2cda5c4d1efe)
- [A Deep Look at Uploading Data to Amazon S3](https://cloud.netapp.com/blog/aws-s3-a-deep-look-at-uploading-data)
