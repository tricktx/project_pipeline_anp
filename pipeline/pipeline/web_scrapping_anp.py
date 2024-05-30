import requests
import pandas as pd
from constants import constants
import os

def download_files(urls: str, path: str) -> None:
    os.system(f"mkdir -p {path}")
    for url in urls:
        r = requests.get(url)
        with open (path, 'wb') as f:
            f.write(r.content)
        
download_files(constants.URLS.value, constants.path.value)
