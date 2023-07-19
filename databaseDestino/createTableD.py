import pyodbc

# Establecer la conexión 
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=jhonglidden;'
    'DATABASE=sqlproconty;'
    'UID=pro;'
    'PWD=1123;'
)


cursor = conn.cursor()

# Definir la consulta SQL para crear la tabla
create_table_query = '''
CREATE TABLE datadestino (
        Company VARCHAR(100),
        Date VARCHAR(100),
        Closep VARCHAR(100),
        Volume VARCHAR(100),
        Openp VARCHAR(100),
        High VARCHAR(100),
        Low VARCHAR(100)
)
'''

cursor.execute(create_table_query)
# Confirmar los cambios
conn.commit()
# Cerrar
cursor.close()
conn.close()



