
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class Result():
    
    def __init__(self, dfsamples,dfmeans, geojson):
        self.dfsamples = dfsamples
        self.dfmeans = dfmeans
        self.geojson = geojson
        

    def plot_total(self):
        ## main plots
        fig = px.choropleth(data_frame=self.dfsamples, 
                    geojson=self.geojson, 
                    locations='departamento', # nombre de la columna del Dataframe
                    featureidkey='properties.NOMBRE_DPT',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='muestras', #El color depende de las cantidades
                    color_continuous_scale="Blues", #greens
                    #scope="north america"
                   )
        fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

        fig.update_layout(
            title_text='Muestras Multilab Agroanalítica 2019',
            autosize=False,
            width=1000,
            height=600,
            )
        return fig
        
        
    def plot_element(self,element):
        ## main plots
        fig = px.choropleth(data_frame=self.dfmeans, 
                    geojson=self.geojson, 
                    locations='departamento', # nombre de la columna del Dataframe
                    featureidkey='properties.NOMBRE_DPT',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color=element, #El color depende de las cantidades
                    color_continuous_scale="Blues", #greens
                    #scope="north america"
                   )
        fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

        fig.update_layout(
            title_text='Promedio de ' + element + " por departamento",
            width=1000,
            height=600,
            )
        return fig
    
        
    