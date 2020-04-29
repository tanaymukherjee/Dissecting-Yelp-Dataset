# Automating data directly into S3 using Kaggle APIs

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

