# Downloading the data
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

# URL of the web page containing the data table
url = 'https://github.com/K-A-Reddy/Housing '

# Load the table into a DataFrame
tables = pd.read_html(url)
data_table = tables[0]  # Assuming the table you want is the first one on the page

# Display the first few rows of the DataFrame
print(data_table.head())