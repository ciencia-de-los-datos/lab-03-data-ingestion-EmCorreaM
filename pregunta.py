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
    
    ruta_archivo = 'clusters_report.txt'
    df = pd.read_csv(ruta_archivo, sep='\s+', skiprows=2, engine='python') # Añadir engine='python' para evitar el error de tokenizing
    df.columns = ['Cluster', 'Cantidad_de_palabras_clave', 'Porcentaje_de_palabras_clave', 'Principales_palabras_clave']
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['Principales_palabras_clave'] = df['Principales_palabras_clave'].str.replace('\s+', ' ').str.strip()
    return df

