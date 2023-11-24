import argparse
import pandas as pd
from fuzzywuzzy import process

# Acceder a los dataframe finales

def dataframes(categoria):
    df_bicimad =  pd.read_csv('./data/interes_bicimad_v02.csv')
    df_bicipark = pd.read_csv('./data/interes_bicipark_v02.csv')

    if categoria == 'Bicimad':
        print(f'legiste: {categoria}')
        print(df_bicimad)
    elif categoria == 'Bicipark':
        print(f'Elegiste: {categoria}')
        print(df_bicipark)

# Función para devolver estación más cercana y distancia

def elegir(categoria, sitio):
    df_bicimad =  pd.read_csv('./data/interes_bicimad_v02.csv')
    df_bicipark = pd.read_csv('./data/interes_bicipark_v02.csv')

    bien = []
    x = process.extractOne(sitio, df_bicimad['Place of interest'])
    bien.append(x[0])
    
    print(f'Elegiste: {categoria}')
    print(f'En el lugar: {bien[0]}')
    
    
    if categoria == 'Bicimad':
        print(f'La estación de bicimad más cercana es: {df_bicimad[df_bicimad["Place of interest"]==bien[0]]["Station name"].iloc[0]}')
        print(f'Está ubicada en: {df_bicimad[df_bicimad["Place of interest"]==bien[0]]["Station address"].iloc[0]}')
        print(f'En esta distancia: {df_bicimad[df_bicimad["Place of interest"]==bien[0]]["Recorrido"].iloc[0]} metros')
        
    elif categoria == 'Bicipark':
        print(f'La estación de bicipark más cercana es: {df_bicipark[df_bicipark["Place of interest"]==bien[0]]["Station name"].iloc[0]}')
        print(f'Está ubicada en: {df_bicipark[df_bicipark["Place of interest"]==bien[0]]["Station address"].iloc[0]}')
        print(f'En esta distancia: {df_bicipark[df_bicipark["Place of interest"]==bien[0]]["Recorrido"].iloc[0]} metros')
       
    else:
        return('Elige entre Bicimad y Bicipark')
    

# Argument parser function

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= '¿Estás buscando la estación de BiciMad más cercana a tu ubicación? ¡Te indicamos cuál es!' )
    parser.add_argument('-r', '--resumen', type=str, help='Escoge entre Bicimad o Bicipark')
    parser.add_argument('-c', '--categoria', type=str, help='Escoge entre Bicimad o Bicipark')
    parser.add_argument('-u', '--ubicacion', type=str, help='A través de la opción "ubicacion" puedes indicar cuál es tu ubicación de origen')
    args = parser.parse_args()
    
    
    if args.resumen != None:
        dataframes(args.resumen)
    elif args.resumen == None:
        elegir(args.categoria, args.ubicacion)