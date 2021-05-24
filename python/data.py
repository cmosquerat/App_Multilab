
import pandas as pd
from settings import config
import geopandas as gpd
import numpy as np
import difflib


class Data():
    
    def get_data(self):
        self.df = pd.read_excel(config.root+"/application/static/" + config.data)
        self.geojson = gpd.read_file(config.root+"/application/static/" + config.geojson)
        self.elementos =  [ele for ele in self.df.columns.tolist() if ele not in config.not_elements]



    @staticmethod
    def change_names(input_pandas,desired_names,columnstring):
        column_values = input_pandas[columnstring].values
        for values in column_values:
            desired_name = difflib.get_close_matches(values, desired_names)
            input_pandas = input_pandas.replace(values, desired_name[0])
        return input_pandas


    def preprocess_samples(self):
        self.df.columns = map(str.lower, self.df.columns) # Se ponen todas los nombres de las columnas en lowercase (Algunos dataset de multilab están en mayúscula)
        f_da = self.df['departamento'].value_counts().reset_index()
        f_da.columns = ['departamento',"muestras"]
        muestras = f_da.replace("Bogotá", "CUNDINAMARCA")
        muestras['departamento'] = muestras['departamento'].str.upper()
        final = self.change_names(muestras,self.geojson["NOMBRE_DPT"].values,"departamento")
        return final

    def multilab_preprocess_means(self):
        self.df.columns = map(str.lower, self.df.columns)
        self.df = self.df.replace("Bogotá", "CUNDINAMARCA")
        self.df['departamento'] = self.df['departamento'].str.upper()
        self.df = self.change_names(self.df,self.geojson["NOMBRE_DPT"].values,"departamento")
        df_output = self.df.groupby('departamento').mean()
        return df_output.reset_index()


