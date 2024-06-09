import pandas as pd
import os
from google.cloud import storage
from pipeline.pipeline.web_scrapping_anp import main
def upload_files(bucket_name: str, local_path: str, gcs_path: str) -> None:

    