import requests as rq
import pandas as pd
import numpy as np
import json
import zipfile

# General variables:
file_path = '' # path to file will sended at webService.
json_output_path = './newOutput.json' # path to output formatted data.
zip_output_path = './zipoutput.zip' # path to Output zipFile.


organization = '' # Id of the organization that will send data.
url_base = '' # URL base of the endpoint that will send data.
service = '' # Service of the endpoint.
access_token = '' # Autentication bearer or any token that service request to receive data.

# Tools e Functions:

def dataFormat(input_path = str, output_path = str):
    replace = [None]
    
    if '.csv' in input_path:
        dfData = pd.read_csv(input_path, delimiter=';', )
    elif '.json' in input_path:
        dfData = pd.read_json(input_path)
    elif '.xlsx' in input_path:
        dfData = pd.read_json(input_path)
        
    dfData.fillna(value= '', inplace=True)
    
    data = {}

    filename_json = output_path
    cont = 0

    for key, val in dfData('Caso'):
        data["dataItems"] = dfData.to_dict('records')


    with open(filename_json, 'w', encoding='utf-8') as outfile:
        json.dump(data, fp= outfile, ensure_ascii=False)
        
    outfile.close()

# Data Formatting:

dataFormat(file_path, json_output_path)


# Data compress to zip:

zip = zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED)
zip.write(json_output_path)
zip.close()

#Requisition compile:


files = [('dataItems',('file', open(zip_output_path, 'rb'), 
         'application/octet-stream'))
         ]

headers = {
    'groupId': organization,
    'Accept': 'application/json',
    'Authorization': access_token
}

requisicao = rq.request('POST', url = url_base+service, headers = headers, files = files)
print(requisicao.text)

print('done')