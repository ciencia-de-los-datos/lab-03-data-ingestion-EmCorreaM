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
        lines = file.readlines()[4:]

    data = []
    current_row = ''
    for line in lines:
        line_strip = line.strip()
        if not line_strip:
            if current_row:
                data.append(current_row)
                current_row = ''
        else:
            current_row += ' ' + line_strip

    if current_row:
        data.append(current_row)

    df = pd.DataFrame(data, columns=['Columna'])
    df['Columna'] = df['Columna'].str.replace(r'\s+%', '', regex=True)
    df['Columna'] = df['Columna'].apply(lambda x: x.strip() if x.isnumeric() else x)
    df = df.replace(r'\s+', ' ', regex=True)
    df['Columna'] = df['Columna'].str.replace(' ', '', 1)
    df = df['Columna'].str.split(' ', n=3, expand=True)

    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.')
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '')
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['cluster'] = df['cluster'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)

    return df
df = ingest_data()
print(df.cluster.to_list())