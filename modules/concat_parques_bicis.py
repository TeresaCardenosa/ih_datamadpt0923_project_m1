# Traer los dataframe de los otros arhivos

from parques_jardines import df 
from bicimad import df_concat
from bicipark import df_concat2

# Traer las funciones de geo_calculations
from geo_calculations import distance_meters

# Unión DF parques y bicimad

df_big = df.merge(df_concat, how='cross')

# Genero una nueva columna + apply lambda función distance meters para tener todos los recorridos

df_big['Recorrido'] = df_big.apply(lambda row: distance_meters(row['Latitude_p'], row['Longitude_p'], row['Latitude'], row['Longitude']), axis=1)

# Ordeno por parque y recorrido
df_big_sorted = df_big.sort_values(by=['Place of interest', 'Recorrido'], ignore_index=True)  

# Genero Serie de Pandas con groupby 

min_value = df_big_sorted.groupby('Place of interest')['Recorrido'].min() 
min_value

# Mergeo la serie

df_big_merge = df_big_sorted.merge(min_value, on='Place of interest',suffixes=('', '_min'))
df_big_merge

# Filtro por recorrido

df_big_merge = df_big_merge[df_big_merge.Recorrido==df_big_merge.Recorrido_min].drop('Recorrido_min', axis=1)

# Limpio columnas

df_big_merge = df_big_merge[['Place of interest', 'Place address', 'Station name', 'Station address', 'Recorrido']]

# Reset index

df_big_merge = df_big_merge.reset_index().drop('index', axis=1)

# Compruebo

print(df_big_merge)

# Exporto a CSV

df_big_merge.to_csv('../data/interes_bicimad.csv')


# Mismo proceso para bicipark

df_big2 = df.merge(df_concat2, how='cross')
df_big2['Recorrido'] = df_big2.apply(lambda row: distance_meters(row['Latitude_p'], row['Longitude_p'], row['Latitude'], row['Longitude']), axis=1)
df_big_sorted2 = df_big2.sort_values(by=['Place of interest', 'Recorrido'], ignore_index=True)  
min_value2 = df_big_sorted2.groupby('Place of interest')['Recorrido'].min() 
min_value2
df_big_merge2 = df_big_sorted2.merge(min_value2, on='Place of interest',suffixes=('', '_min'))
df_big_merge2
df_big_merge2 = df_big_merge2[df_big_merge2.Recorrido==df_big_merge2.Recorrido_min].drop('Recorrido_min', axis=1)
df_big_merge2 = df_big_merge2[['Place of interest', 'Place address', 'Station name', 'Station address', 'Recorrido']]
df_big_merge2 = df_big_merge2.reset_index().drop('index', axis=1)

# Compruebo

print(df_big_merge2)

# Exporto a CSV

df_big_merge2.to_csv('../data/interes_bicipark.csv')

