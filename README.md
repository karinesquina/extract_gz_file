This code load, extract and save GZ files whit Python.

You can replace the URL, and your local path.

**Libs**
from pip._vendor import requests
from io import BytesIO
import gzip
from pathlib import Path
import shutil
import zipfile
import os
