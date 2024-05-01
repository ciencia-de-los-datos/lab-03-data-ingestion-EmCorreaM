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
    # Lee el archivo 'clusters_report.txt' y separa las líneas
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Procesa las líneas para formar filas del DataFrame
    data = []
    for line in lines:
        # Divide cada línea en palabras clave separadas por coma
        keywords = line.strip().split(',')
        # Formatea las palabras clave con un solo espacio entre palabra y palabra
        formatted_keywords = ', '.join(keyword.strip() for keyword in keywords)
        data.append(formatted_keywords)

    # Construye el DataFrame
    df = pd.DataFrame(data, columns=['keywords'])

    # Cambia los nombres de las columnas a minúsculas y reemplaza espacios por guiones bajos
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    return df

# Llama a la función para obtener el DataFrame
df = ingest_data()
print(df)