"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Eliminar espacios en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Convertir las columnas de texto a minúsculas
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
 # Eliminar duplicados
   

    # Lidiar con datos faltantes
    df.dropna(inplace=True)

    # Convertir la columna 'fecha_de_beneficio' al formato de fecha
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, errors='coerce')

    # Limpiar la columna 'monto_del_credito' eliminando caracteres no numéricos
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('[^\d.]', '', regex=True).astype(float)

    df['idea_negocio'] = df['idea_negocio'].str.replace('[-_]', ' ', regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.strip()
    df['barrio'] = df['barrio'].str.replace('[-_]', ' ', regex=True)
    df['barrio'] = df['barrio'].str.strip()
    # Convertir la columna 'estrato' a tipo entero
    df['estrato'] = df['estrato'].astype(int)
    df.drop_duplicates( inplace=True)
   
    
    # Restablecer los índices después de eliminar filas
    df.reset_index(drop=True, inplace=True)
    

    return df
