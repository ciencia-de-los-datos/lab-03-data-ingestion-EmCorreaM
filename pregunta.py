"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    with open('clusters_report.txt', 'r') as archivo:
        lineas = archivo.readlines()

    datos = []

    for linea in lineas:
        if not linea.startswith('-'):
            columnas = linea.split()

            if len(columnas) > 1:
                cluster = columnas[0]
                cantidad_palabras_clave = columnas[1]
                porcentaje_palabras_clave = columnas[2]
                palabras_clave = ' '.join(columnas[3:]).replace(',', ', ')

                datos.append([cluster, cantidad_palabras_clave, porcentaje_palabras_clave, palabras_clave])

    df = pd.DataFrame(datos, columns=['cluster', 'cantidad_palabras_clave', 'porcentaje_palabras_clave', 'palabras_clave'])

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    return df

df = ingest_data()
print(df)