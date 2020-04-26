# Converting JSON to CSV

This part is not part of the original exercise as wirth AWS S3 we can easily load gigabytes of data in no time and use it for our analysis while distritbuting the task through multiple nodes and optimising the process using spark.

However, as part of analysis I converted JSON to CSV and it was a great learning experience. Though, the main analysis will be done using JSON only on EC2.

## A) Methods to concert JSON to CSV
### 1. Generic Method:

* ```json_to_csv_generic.py```
``` 
It parses the json file by first identifying the encoding - whether it is UTF-8 encoding or a normal one.
- First we read the JSON content
- Then load an empty CSV file
- Load the JSON content
- Close the input file once we have read each key/value pair
- Write in the CSV file
```

### 2. Yelp Dataset Method:

* ```json_to_csv_yelp.py```
``` 
It parses the json file by first identifying the encoding - whether it is UTF-8 encoding or a normal one.
- First we read the JSON content
- Then load an empty CSV file
- Load the JSON content
- Close the input file once we have read each key/value pair
- Write in the CSV file

All the above steps are same as the generic one, however, the yelp dataset is a complex one, as there are dicts inside dicts

Thus, we have to write a complex loop structure to ensure the conversion is done correctly.

We must flatten one dict at a time and then flatten each record before running a loop for the same
```

## C) Loading data into S3 bucket
### 1. AWS S3 buck configuration
![s3 data bucket_csv](https://user-images.githubusercontent.com/6689256/80297017-7564e700-874d-11ea-8835-b8a818ed6c58.png)
