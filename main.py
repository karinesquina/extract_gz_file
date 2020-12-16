from pip._vendor import requests
from io import BytesIO
import gzip
from pathlib import Path
import shutil
import zipfile
import os

url = "https://data.brasil.io/dataset/covid19/boletim.csv.gz"
folder = Path('.') / 'raw' / 'extract.csv' 

def save_file(folder_name, file_descompact):
    os.makedirs(os.path.dirname(folder_name), exist_ok=True)
    with open(folder_name, 'w') as file_out:
        file_out.write(file_descompact)

def extract_gzfile(link):
    r = requests.get(link)
    file_compress = BytesIO(r.content)
    file_descompress = gzip.GzipFile(fileobj=file_compress)
    save_file(folder, str(file_descompress.read()))

extract_gzfile(url)

