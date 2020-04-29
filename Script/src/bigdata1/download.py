import os
import kaggle
import sys
import pandas as pd
import numpy as np
import requests
from requests import HTTPError

# The API from where we are trying to call the dataset
domain = "data_url"

# Printing the domian and session details
print("Domain: {domain:}\nSession: {session:}\nURI Prefix: {uri_prefix:}".format(**client.__dict__))

# Call the api_token for kaggle
app_id = os.environ.get("KAGGLE_USERNAME")
app_key = os.environ.get("KAGGLE_TOKEN")

# The local path where the data set is saved.
local_filename = "file_name"

# Kaggle Username and Password
kaggle_info = {'UserName': app_id, 'Password': app_key}

# Attempts to download the CSV file. Gets rejected because we are not logged in.
r = requests.get(domain)

# Login to Kaggle and retrieve the data.
r = requests.post(r.url, data = kaggle_info, prefetch = False)

# Writes the data to a local file one chunk at a time.
f = open(local_filename, 'w')

# Reads 512KB at a time into memory
for chunk in r.iter_content(chunk_size = 512 * 1024): 
    if chunk: 
    # filter out keep-alive new chunks
        f.write(chunk)
f.close()

# Utility methods for exception handling
def raise_for_status(response):

    # Custom raise_for_status with more appropriate error message.
    http_error_msg = ""

    if 400 <= response.status_code < 500:
        http_error_msg = "{0} Client Error: {1}".format(
            response.status_code, response.reason
        )

    elif 500 <= response.status_code < 600:
        http_error_msg = "{0} Server Error: {1}".format(
            response.status_code, response.reason
        )

    if http_error_msg:
        try:
            more_info = response.json().get("message")
        except ValueError:
            more_info = None
        if more_info and more_info.lower() != response.reason.lower():
            http_error_msg += ".\n\t{0}".format(more_info)
        raise requests.exceptions.HTTPError(http_error_msg, response=response)   
