
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class Result():
    
    def __init__(self, df_depto,df_mun, geojson_depto,geojson_mun):
        self.df_depto = df_depto
        self.df_mun = df_mun
        self.geojson_depto = geojson_depto
        self.geojson_mun = geojson_mun

    def plot_total(self,location):

        if location is not None:
            selected_mun = self.df_mun[self.df_mun["departamento"].str.contains(location)]

            fig = px.choropleth(data_frame=selected_mun, 
                geojson=self.geojson_mun, 
                locations='municipio', # nombre de la columna del Dataframe
                featureidkey='properties.MPIO_CNMBR',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                color='muestras', #El color depende de las cantidades
                color_continuous_scale=["white", "#1226AA"], #greens
                hover_name="municipio",
                hover_data={'municipio':False}
                #scope="north america"
                )
            fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

            fig.update_layout(
                title_text='Muestras Multilab Agroanalítica 2019 (MPIO)',
                autosize=False,
                width=1000,
                height=600,
                hoverlabel=dict(
                    bgcolor="#870064",
                
                    
                )
                )


        else: 
        ## main plots
            fig = px.choropleth(data_frame=self.df_depto, 
                        geojson=self.geojson_depto, 
                        locations='departamento', # nombre de la columna del Dataframe
                        featureidkey='properties.NOMBRE_DPT',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                        color='muestras', #El color depende de las cantidades
                        color_continuous_scale=["white", "#1226AA"], #greens
                        hover_name="departamento",
                        hover_data={'departamento':False}
                        #scope="north america"
                        )
            fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

            fig.update_layout(
                title_text='Muestras Multilab Agroanalítica 2019',
                autosize=False,
                width=1000,
                height=600,
                hoverlabel=dict(
                    bgcolor="#870064",
                    
                    
                )
                )
        return fig


    def plot_mun(self):

        

        ## main plots
        fig = px.choropleth(data_frame=self.df_mun, 
                    geojson=self.geojson_mun, 
                    locations='municipio', # nombre de la columna del Dataframe
                    featureidkey='properties.MPIO_CNMBR',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='muestras', #El color depende de las cantidades
                    color_continuous_scale=["white", "#1226AA"], #greens
                    hover_name="municipio",
                    hover_data={'municipio':False}
                    #scope="north america"
                   )
        fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

        fig.update_layout(
            title_text='Muestras Multilab Agroanalítica 2019 (MPIO)',
            autosize=False,
            width=1000,
            height=600,
            hoverlabel=dict(
                bgcolor="#870064",
               
                
            )
            )
        return fig  

    def plot_elemnt_mun(self,element):
       
        if "Rangos" not in element:
            element = element
            hover = "Rangos " + element
            Title = 'Promedio de ' + element + " por municipio"
        else: 
            hover = element
            element = "Rango moda " + element.replace("Rangos ", "")
            Title = hover + " mpio"


        fig = px.choropleth(data_frame=self.df_mun, 
                    geojson=self.geojson_mun, 
                    locations='municipio', # nombre de la columna del Dataframe
                    featureidkey='properties.MPIO_CNMBR',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color=element, #El color depende de las cantidades
                    color_continuous_scale=["white", "#1226AA"], #greens
                    hover_name="municipio",
                    hover_data={'municipio':False,
                    hover: True,
                    hover.replace("Rangos ",""):':.2f'}
                    #scope="north america"
                   )
        fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

        fig.update_layout(
            title_text=Title,
            autosize=False,
            width=1000,
            height=600,
            hoverlabel=dict(
                bgcolor="#870064",
               
                
            )
            )
        return fig     
        
        
    def plot_element(self,element):

        if "Rangos" not in element:
            element = element
            hover = "Rangos " + element
            Title = 'Promedio de ' + element + " por departamento"
        else: 
            hover = element
            element = "Rango moda " + element.replace("Rangos ", "")
            Title = hover
            

        

        ## main plots
        fig = px.choropleth(data_frame=self.df_depto, 
                    geojson=self.geojson_depto, 
                    locations='departamento', # nombre de la columna del Dataframe
                    featureidkey='properties.NOMBRE_DPT',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color=element, #El color depende de las cantidades
                    color_continuous_scale=["white", "#1226AA"], #greens
                    hover_name="departamento",
                    hover_data={'departamento':False,
                    hover: True,
                    hover.replace("Rangos ",""):':.2f'}
                   )
        fig.update_geos(showcountries=True, showcoastlines=False, showland=False, fitbounds="locations")

        fig.update_layout(
            title_text=Title,
            width=1000,
            height=600,
            hoverlabel=dict(
                bgcolor="#870064",
                
                
            )
            )
        return fig
    
        
    