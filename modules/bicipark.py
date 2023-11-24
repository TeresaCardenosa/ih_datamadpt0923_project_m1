# Librerias

import pandas as pd


# Generar DF 

df_previo2 = pd.read_csv('./data/bicipark_stations.csv', sep=";")

df_previo2 = df_previo2[['stationName', 'address', 'geometry.coordinates']]


# Split de columna 'geometry.coordinates' + drop de la columna anterior + rename de las columnas 

split2 = df_previo2['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype("float64")
split2.columns = ['Longitude', 'Latitude']

df_concat2 = pd.concat([df_previo2, split2], axis=1)

df_concat2 = df_concat2.drop(['geometry.coordinates'], axis=1)

df_concat2 = df_concat2.rename(columns = {'stationName': 'Station name', 'address': 'Station address'})

print(df_concat2)