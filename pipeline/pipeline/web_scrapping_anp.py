import requests
import pandas as pd
from constants import constants
import os

def download_files(urls: str) -> None:
    os.makedirs(constants.INPUT.value, exist_ok=True)
    for url in urls:
        # Verify=False is necessary to avoid SSL verification, look:
        ##  https://requests.readthedocs.io/projects/pt/pt-br/latest/user/advanced.html
        ##  https://www.cloudflare.com/pt-br/learning/ssl/what-is-an-ssl-certificate/
        r = requests.get(url, verify=False, headers=constants.HEADERS.value)
        file_name = url.split('/')[-1]
        path_file = os.path.join(constants.INPUT.value, file_name)
        with open(path_file, 'wb') as f:
            f.write(r.content)

def concat_files() -> pd.DataFrame:
    download_files(constants.URLS.value)
    df_total = []
    for paths in constants.PATH.value:
        df = pd.read_csv(paths, sep=';', encoding='utf-8')
        df_total.append(df)

        df = pd.concat(df_total, ignore_index=False)

    return df

def partition_data(df: pd.DataFrame) -> None:
    for year in df['Data da Coleta'].str[6:10].unique():


        for sigla in df['Estado - Sigla'].unique():

            partition = os.makedirs(f'{constants.OUTPUT.value}/{year}/{sigla}', exist_ok=True)
            df_partition = df[(df['Data da Coleta'].str[6:10].unique()) & (df['Estado - Sigla'] == sigla)]
            df_partition.drop(columns = ['Data da Coleta', 'Estado - Sigla'], inplace=True)
            df_partition_path = f'{constants.OUTPUT.value}/{year}/{sigla}/data.csv'
            df_partition.to_csv(df_partition_path, encoding='utf-8', index=False, na_rep = '')

def main() -> None:
    df = concat_files()
    partition_data(df)

main()