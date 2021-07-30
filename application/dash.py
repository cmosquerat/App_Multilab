###############################################################################
#                                MAIN                                         #
###############################################################################

# Setup
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from settings import config, about
from python.data import Data
from python.result import Result



# Read data
data = Data()
data.get_data()

df_depto = data.df_dep

df_mun =  data.df_mun

geojson_dpto = data.geojson_depto

geojson_mun = data.geojson_mun

result = Result(df_depto,df_mun,geojson_dpto,geojson_mun)

n_muestras = sum(df_depto['muestras'])
print(n_muestras)
n_deptos = len(df_depto.index)
n_mun = data.df_mun["municipio"].nunique()



# App Instance


app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.PULSE, config.fontawesome],suppress_callback_exceptions=True,)
app.title = "Mapas de fertilidad de suelos de Colombia"





# Navbar
titulo = dbc.Row(children=[
    html.H1(
                        html.B("Mapas de fertilidad de suelos de Colombia"),
                        style={"color": "#1226AA"},
                    ),
    
    html.Img(src=app.get_asset_url("Logo_slogan.jpg"), height="150px"),

], justify="center", align="center")


imagen = dbc.Row(children=[

    html.Img(src=app.get_asset_url("Logo_slogan.jpg"), height="100px"),

], justify="center", align="center")


# Input
inputs = dbc.FormGroup([
    html.H4("Seleccionar tipo de muestra"),
    dcc.Dropdown(id="country", options=[{"label":x,"value":x} for x in data.elementos], value="ph")
]) 



# App Layout

'''
app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    titulo,
    html.Br(),
    

    ## Body
    dbc.Row([
        ### input + panel
        
        ### plots
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Georreferenciados por nutrimentos para cultivos en departamentos y municipios:"), width={"size":20,"offset":3}), 
            html.Br(),
            dbc.Tabs(className="nav nav-pills", children=
            [
                dbc.Tab(label="Elemento Químico Depto", tab_id="tab-1",active_label_style={"background": "#1226AA"},tabClassName="flex-grow-1 text-center"),
                dbc.Tab(label="Elemento Químico Mpio", tab_id="tab-4",active_label_style={"background": "#1226AA"},tabClassName="flex-grow-1 text-center"),
                dbc.Tab(label="Muestras Depto", tab_id="tab-2",active_label_style={"background": "#1226AA"},tabClassName="flex-grow-1 text-center"),
                dbc.Tab(label="Muestras Mpio", tab_id="tab-3",active_label_style={"background": "#1226AA"},tabClassName="flex-grow-1 text-center"),
            ],
            id="tabs",
            active_tab="tab-1",
            
        ),
            html.Br(),
            inputs,
            html.Br(),
            
        
         html.Div(id="content"),
         dbc.Col(html.H5("Multilab Agroanalítica entrega conocimiento técnico y científico para la toma de decisiones del sector agroindustrial de Colombia"), width={"size":25,"offset":3}), 
        ])
    ],justify="center", align="center")
])


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return dbc.Row(dcc.Graph(id="plot-total"),justify="center", align="center")
    elif at == "tab-2":
        return dbc.Row(dcc.Graph(id="plot-active"),justify="center", align="center")
    elif at == "tab-3":
        return dbc.Row(dcc.Graph(id="plot-mun"),justify="center", align="center")
    elif at == "tab-4":
        return dbc.Row(dcc.Graph(id="plot-emun"),justify="center", align="center")
        
        
'''



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


app1 = dbc.Row(
    
    children=[dcc.Graph(id="plot-total"),inputs]
    ,justify="center", align="center")



app2 = dbc.Row(
    
    children=[dcc.Graph(id="plot-active")]
    ,justify="center", align="center")

app3 = dbc.Row(
    
    children=[dcc.Graph(id="plot-mun")]
    ,justify="center", align="center")

app4 = dbc.Row(
    
    children=[dcc.Graph(id="plot-emun"),inputs]
    ,justify="center", align="center")




@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/uno':
        return app1
    if pathname == '/dos':
        return app2
    if pathname == '/tres':
        return app3
    if pathname == '/cuatro':
        return app4
    else:
        return "404"

'''
# Python functions for about navitem-popover
@app.callback(output=Output("about","is_open"), inputs=[Input("about-popover","n_clicks")], state=[State("about","is_open")])
def about_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(output=Output("about-popover","active"), inputs=[Input("about-popover","n_clicks")], state=[State("about-popover","active")])
def about_active(n, active):
    if n:
        return not active
    return active




'''
@app.callback(output=Output("plot-total","figure"), inputs=[Input("country","value"),Input("plot-total","clickData")])
def plot_total_cases1(country,clickData):
    if clickData is not None:
        return result.plot_element(country,clickData['points'][0]['location'])
    else: 
        return result.plot_element(country,None)







@app.callback(output=Output("plot-active","figure"), inputs=[Input("plot-active","clickData")])
def plot_active_cases2(clickData):
    if clickData is not None:
        return result.plot_total(clickData['points'][0]['location'])
    else: 
        return result.plot_total(None)





    
    



@app.callback(output=Output("plot-mun","figure"), inputs=[Input("plot-mun","clickData")])
def plot_active_cases3(clickData):
    return result.plot_mun()


@app.callback(output=Output("plot-emun","figure"), inputs=[Input("country","value")])
def plot_active_cases4(country):
    return result.plot_elemnt_mun(country)

'''
@app.callback(output=Output("output-panel","children"), inputs=[Input("country","value")])
def render_output_panel(country):
    panel = dbc.Row(html.Div([
        dbc.Card(body=True, className="text-white",style={"background":"#1226AA","width": "25rem"}, children=[
            
            html.H6("Total muestras procesadas", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_muestras), style={"color":"white"}),
            
            html.H6("Número de departamentos en los que se tiene presencia", style={"color":"#80BC00"}),
            html.H3("{:,.0f}".format(n_deptos), style={"color":"#80BC00"}),
            
            html.H6("Número de municipios en los que se tiene presencia", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_mun), style={"color":"white"}),
        
        ])
    ]),justify="center", align="center")
    return panel
'''