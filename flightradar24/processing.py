import pandas as pd
path='./data/'
df1=pd.read_parquet(path + 'airlines.parquet', engine='fastparquet')
df2=pd.read_parquet(path + 'airports.parquet', engine='fastparquet')
df3=pd.read_json(path + 'zones.json')
print(df3.head(4))

import json
# load data using Python JSON module
with open(path + 'zones.json','r') as f:
    data = json.loads(f.read())
# Flatten data
df = pd.json_normalize(data, record_path =['subzones'],meta=[
        'europe'
        
    ])
print(df.head())

'''
['info', 'president'], 
        ['info', 'contacts', 'tel']'''