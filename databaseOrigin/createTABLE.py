import psycopg2
from psycopg2 import sql





# class Pgbase:
#     def __init__(self, host, port=5432, database,user, password):
#         self.host=host
#         self.port=port
#         self.database=database
#         self.__user=user
#         self.__pasword=pasword

#     def conect_cursor(self):

        





# Parámetros de conexión a tu base de datos
params = {
    "host"      : "localhost",
    "port"      : "5432",
    "database"  : "proconty",
    "user"      : "postgres",
    "password"  : "172314"
}

# Conectarse a la base de datos
conn = psycopg2.connect(**params)

# Crear un cursor
cur = conn.cursor()


# Create the table
cur.execute("""
CREATE TABLE IF NOT EXISTS dataprueba (
        Company VARCHAR(100),
        Date VARCHAR(100),
        Close VARCHAR(100),
        Volume VARCHAR(100),
        Open VARCHAR(100),
        High VARCHAR(100),
        Low VARCHAR(100)
)""")



conn.commit()
# Close the cursor object
cur.close()

# Close the connection to the database
conn.close()



