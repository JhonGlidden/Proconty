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

        





# Parámetros 
params = {
    "host"      : "localhost",
    "port"      : "5432",
    "database"  : "proconty",
    "user"      : "postgres",
    "password"  : "172314"
}


conn = psycopg2.connect(**params)

# Crear un cursor
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS dataorigen (
        Company VARCHAR(100),
        Date VARCHAR(100),
        Closep VARCHAR(100),
        Volume VARCHAR(100),
        Openp VARCHAR(100),
        High VARCHAR(100),
        Low VARCHAR(100)
)""")



conn.commit()

cur.close()

conn.close()



