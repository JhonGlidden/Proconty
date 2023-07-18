import pandas as pd
import numpy as np 




class Archivo:
    def __init__(self,path_file):
        self.path_file=path_file
        self.data=None

class ArchivoCSV(Archivo):
    def read_data(self):
        self.data=pd.read_csv(self.path_file)



archivo_kagle=ArchivoCSV('CVD_cleaned.csv')
archivo_kagle.read_data()

print(archivo_kagle.data)








