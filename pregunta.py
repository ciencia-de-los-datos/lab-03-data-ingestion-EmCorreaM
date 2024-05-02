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
    with open("clusters_report.txt", 'r') as file:
        lineas = file.readlines()[4:]

    data = []
    fila_actual = ''
    for linea in lineas:
        linea_strip = linea.strip()
        if not linea_strip:
            if fila_actual:
                data.append(fila_actual.strip())
                fila_actual = ''
        else:
            fila_actual += ' ' + linea_strip

    if fila_actual:
        data.append(fila_actual.strip())

    df = pd.DataFrame(data, columns=['Columna'])
    df['Columna'] = df['Columna'].str.replace(r'\s+%', '', regex=True)
    df['Columna'] = df['Columna'].str.strip().apply(lambda x: x if x.isdigit() else x.strip())
    df = df['Columna'].str.replace(r'\s+', ' ').str.split(' ', n=3, expand=True)

    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.')
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '')
    df[['cantidad_de_palabras_clave', 'cluster']] = df[['cantidad_de_palabras_clave', 'cluster']].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)

    return df