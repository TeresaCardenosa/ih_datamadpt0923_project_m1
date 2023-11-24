# Librerias

import pandas as pd


# Generar DF 

df_previo = pd.read_csv('./data/bicimad_stations.csv', sep="\t")

df_previo = df_previo[['name', 'address', 'geometry.coordinates']]


# Split de columna 'geometry.coordinates' + drop de la columna anterior + rename de las columnas 

split = df_previo['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype("float64")
split.columns = ['Longitude', 'Latitude']

df_concat = pd.concat([df_previo, split], axis=1)

df_concat = df_concat.drop(['geometry.coordinates'], axis=1)

df_concat = df_concat.rename(columns = {'name': 'Station name', 'address': 'Station address'})

print(df_concat)