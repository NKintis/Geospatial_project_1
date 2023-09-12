import os
import zipfile

username = 'thanasisdrivas'
password = 'Nopassaran123'

from hda import Client, Configuration
from pathlib import Path

var1 = float(os.environ.get('VAR1'))
var2 = float(os.environ.get('VAR2'))
var3 = float(os.environ.get('VAR3'))
var4 = float(os.environ.get('VAR4'))
var5 = os.environ.get('VAR5')
var6 = os.environ.get('VAR6')

bbox = [var1, var2, var3, var4]

# Get start and end dates from environment variables
start_date = var5
end_date = var6

conf = Configuration(user=username, password=password)
hda_client = Client(config=conf)

hdarc = Path(Path.home() / '.hdarc')

if not hdarc.is_file():
    import getpass

    with open(Path.home() / '.hdarc', 'w') as f:
        f.write(f'user:{username}\n')
        f.write(f'password:{password}\n')

query = {
    "datasetId": "EO:ESA:DAT:SENTINEL-2:MSI",
    "boundingBoxValues": [
        {
            "name": "bbox",
            "bbox": bbox
        }
    ],
    "dateRangeSelectValues": [
        {
            "name": "position",
            "start": f"{start_date}T00:00:00.000Z",
            "end": f"{end_date}T00:00:00.000Z"
        }
    ],
    "stringChoiceValues": [
        {
            "name": "processingLevel",
            "value": "S2MSI2A"
        }
    ],
    "stringInputValues": [
        {
            "name": "cloudCover",
            "value": "70"
        }
    ]
}

matches = hda_client.search(query)


matches.download(download_dir="/sample_data/raw")

downloaded_files = matches[0].results

matches = hda_client.search(query)


# Define the directory where you want to extract the contents
extracted_dir = '/sample_data/raw'

#for product in os.listdir(extracted_dir):
#	print(product)
#	if product is not None:
#		os.system(f"unzip {product} {extracted_dir}")
#		print(f'Contents from {product} extracted to {extracted_dir}')
#		os.remove(os.path.join(extracted_dir,product))

for product in os.listdir(extracted_dir):
    print(product)
    if product is not None:
        zip_path = os.path.join(extracted_dir, product)
        os.system(f"unzip {zip_path} -d {extracted_dir}")
        print(f'Contents from {product} extracted to {extracted_dir}')
        os.remove(zip_path)
