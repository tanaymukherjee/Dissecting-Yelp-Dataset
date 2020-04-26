# Dissecting-Yelp-Dataset
*A trove of reviews, businesses, users, tips, and check-in data!*

This dataset is a subset of Yelp's businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. In the dataset you'll find information about businesses across 11 metropolitan areas in four countries.


## Part 1: Installation and Initial Setup
In this portion, we will import the necessary dependencies and load our dataset as a pyspark dataframe.

### A) Installation
* ```Loading data into S3 bucket```
![s3 data bucket](https://user-images.githubusercontent.com/6689256/80295489-ff5a8300-8740-11ea-90cf-35952dd30052.png)

* ```Configuring the EMR cluster```
![EMR cluster](https://user-images.githubusercontent.com/6689256/80295460-c8846d00-8740-11ea-9604-27ad6366b1e9.png)

* ```Initiating notebook instance```
![Notebook instance](https://user-images.githubusercontent.com/6689256/80295518-45174b80-8741-11ea-9b76-5feb1632698f.png)

### B) Initial Setup
* ```Notebook Location```
``` 
xyz
```
* ```Loading data from S3 bucket```
``` 
df = spark.read.json('s3://yelp-dataset-tm/*.json')
```
* ```Load and verify the dependencies```
``` 
sc.list_packages()
```
* ```Overview of the dataset```
``` 
df.printSchema()
```

- [x] This module is completed


## Part 2: Analyzing Categories
For this part, we will take a stab at denormalizing the categories that are associated with each business (there may be more than one, presented as a string of comma separated identifiers) and then running some basic analysis on the result.

* ```Breaking of multiple categories from 'categories' column into multiple rows```
``` 
res = df_2.select(df_2.business_id, explode(split(df_2.categories, ', ')).alias('category'))
```
* ```Total unique categories```
``` 
unique = res.select("category").distinct()
unique.select("category").count()
```
* ```Total categories by business```
``` 
res.groupBy("category").count().show()
```
* ```Top 20 business categories```
``` 
category = df.select('categories')
individual_category = category.select(explode(split('categories', ', ')).alias('category'))
grouped_category = individual_category.groupby('category').count()
top_category = grouped_category.sort('count',ascending=False)
top_category.show(20,truncate=False)
```
* ```Visualization of top 20 business categories```
![bar chart](https://user-images.githubusercontent.com/6689256/80319592-2f586380-87df-11ea-8ada-29c81ca8e6f6.png)

- [x] This module is completed


## Part 3: Do Yelp Reviews Skew Negative?
For this next part, we will attempt to answer the question: 
- Are the (written) reviews generally more pessimistic or more optimistic as compared to the overall business rating.

- [ ] This module is under progress


## Part 4: Should the Elite be Trusted?
For this final part we may choose to either answer this question posed or explore the data in some other manner of own own choosing. The only requirements are:
- We must leverage the users dataset provided
- We must have at least one data visualization as part of your analysis

- [ ] This module is not starterd yet


## Appendix
All the additional info about the project - the tools used, the servers required, system configuration, references, etc are included in this section.

### A) Project Specifications

#### 1. Application Summary
* ```System Specification:```
``` 
Operating System: Windows 10
RAM Size: 16 GB
Memory: 500 GB
```

* ```Tools Used:```
``` 
Programming Language: Python (Version 3.7)
Editor: Jupyter Notebook
Platform: Amazon EMR (Elastic MapReduce)
```

* ```Services Commissioned:```
``` 
Cloud Platform: Amazon Web Services (AWS)
Framework: Apache PySpark
Version Control System: Git
```

#### 2. Communication Channel
* ```Offline:```
``` 
Classrom: Room 10-155
Timing: Friday, 1800 to 2100 Hours
Address: Baruch Vertical Campus,
55, Lexington Avenue,
New York, USA
```

* ```Online:```
``` 
Slack: STA9760
Members: 53
```

### B) References

#### 1. Guide
* ```Prof. Taqqui Karim```
``` 
Subject: 9760 - Big Data Technologies
Session: Spring, 2020
```

#### 2. Links
- [Download Yelp Dataset](https://www.kaggle.com/yelp-dataset/yelp-dataset#yelp_academic_dataset_user.json)
- [Converting JSON to CSV](https://medium.com/@gabrielpires/how-to-convert-a-json-file-to-csv-python-script-a9ff0a3f906e)
- [PySpark Explode](https://sparkbyexamples.com/pyspark/pyspark-explode-array-and-map-columns-to-rows/)
