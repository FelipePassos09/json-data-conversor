import pandas as pd
import json
import numpy as np

replace = [None, None, None, None, None, None, None, None, None]
dfData = pd.read_csv('./Tabela (76).csv', delimiter=';', )
dfData.fillna(value= '', inplace=True)
dfDataAgrupado = dfData
data = {}

filename_json = './dadosFormatado.json'
cont = 0

for key, val in dfDataAgrupado.groupby('Caso'):
    data["eventLog"] = dfDataAgrupado.to_dict('records')
    print(val)
    cont += 1
    print(cont)

with open(filename_json, 'w', encoding='utf-8') as outfile:
    json.dump(data, fp= outfile, ensure_ascii=False)
    
outfile.close()

print(dfData.info)