# import sys
# sys.path.append(".")
# from data.read_data import Archivo

import psycopg2
from psycopg2 import sql
import csv


# Parámetros 
params = {
    "host"      : "localhost",
    "port"      : "5432",
    "database"  : "proconty",
    "user"      : "postgres",
    "password"  : "172314"
}

# 
conn = psycopg2.connect(**params)

#cursor
cursor = conn.cursor()


# Ruta del archivo CSV a cargar
archivo_csv = 'data/data.csv'
nombre_tabla = 'dataorigen'

cursor.execute(f"DELETE FROM {nombre_tabla}")

# Abrir el archivo CSV y leer los datos
with open(archivo_csv, 'r') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        # Insertar cada fila en la tabla
        print(row)
        cursor.execute(
            f"INSERT INTO {nombre_tabla} (Company, Date, Closep, Volume, Openp, High, Low) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        )
conn.commit()
# Cerrar la conexión
cursor.close()
conn.close()