# Librerias

import pandas as pd
import requests
import json


# Petición request para obtener el json

url = 'https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json'
response = requests.get(url)

json_data = response.json()

jsondatagraph = json_data['@graph']

df = pd.json_normalize(jsondatagraph)


# Seleccionar columnas y renombrarlas 

df = df[['title', 'address.street-address', 'location.latitude', 'location.longitude']]

df = df.rename(columns= {'title': 'Place of interest', 'address.street-address': 'Place address', 'location.latitude': 'Latitude_p', 'location.longitude': 'Longitude_p'})

print(df)
