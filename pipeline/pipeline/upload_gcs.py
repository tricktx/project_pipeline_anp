import pandas as pd
import os
from google.cloud import storage
import os


# get the variable environment that contains the path to the service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tricktx/project_pipeline_anp/service_account_anp/anp.json"

# define function that creates the bucket
def create_bucket(bucket_name, storage_class='STANDARD', location='us-central1'): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
   
    bucket = storage_client.create_bucket(bucket, location=location) 
    # for dual-location buckets add data_locations=[region_1, region_2]
    
    return f'Bucket {bucket.name} successfully created.'

create_bucket(bucket_name = 'anp_bucket',
              storage_class='STANDARD',
              location='us-central1')