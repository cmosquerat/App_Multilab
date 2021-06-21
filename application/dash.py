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
app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.PULSE, config.fontawesome])
app.title = "Multilab"



# Navbar
navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
])



# Input
inputs = dbc.FormGroup([
    html.H4("Seleccionar tipo de muestra"),
    dcc.Dropdown(id="country", options=[{"label":x,"value":x} for x in data.elementos], value="ph")
]) 



# App Layout
app.layout = dbc.Container(fluid=True, children=[
    ## Top
    html.H1(config.name, id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),

    ## Body
    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            inputs,
            html.Br(),
            html.Div(id="output-panel")
        ]),
        ### plots
        dbc.Col(md=9, children=[
            dbc.Col(html.H4(""), width={"size":6,"offset":3}), 
            dbc.Tabs(className="nav nav-pills", children=
            [
                dbc.Tab(label="Elemento Químico Depto", tab_id="tab-1",active_label_style={"background": "#1226AA"}),
                dbc.Tab(label="Elemento Químico Mpio", tab_id="tab-4",active_label_style={"background": "#1226AA"}),
                dbc.Tab(label="Muestras Depto", tab_id="tab-2",active_label_style={"background": "#1226AA"}),
                dbc.Tab(label="Muestras Mpio", tab_id="tab-3",active_label_style={"background": "#1226AA"}),
            ],
            id="tabs",
            active_tab="tab-1",
            
        ),
         html.Div(id="content"),
        ])
    ])
])


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return dcc.Graph(id="plot-total")
    elif at == "tab-2":
        return dcc.Graph(id="plot-active")
    elif at == "tab-3":
        return dcc.Graph(id="plot-mun")
    elif at == "tab-4":
        return dcc.Graph(id="plot-emun")
        
        
    




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




@app.callback(output=Output("plot-total","figure"), inputs=[Input("country","value")]) 
def plot_total_cases1(country):
    return result.plot_element(country)






@app.callback(output=Output("plot-active","figure"), inputs=[Input("plot-active","clickData")])
def plot_active_cases2(clickData):
    if clickData is not None:
        return result.plot_total(clickData['points'][0]['location'])
    else: 
        return result.plot_total(None)
    
@app.callback(output=Output("plot-mun","figure"), inputs=[Input("country","value")])
def plot_active_cases3(country):
    return result.plot_mun()

@app.callback(output=Output("plot-emun","figure"), inputs=[Input("country","value")])
def plot_active_cases4(country):
    return result.plot_elemnt_mun(country)

 
@app.callback(output=Output("output-panel","children"), inputs=[Input("country","value")])
def render_output_panel(country):
    panel = html.Div([
        html.H4("Alcance de Multilab"),
        dbc.Card(body=True, className="text-white",style={"background":"#1226AA"}, children=[
            
            html.H6("Total muestras procesadas", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_muestras), style={"color":"white"}),
            
            html.H6("Número de departamentos en los que se tiene presencia", style={"color":"#80BC00"}),
            html.H3("{:,.0f}".format(n_deptos), style={"color":"#80BC00"}),
            
            html.H6("Número de municipios en los que se tiene presencia", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_mun), style={"color":"white"}),
        
        ])
    ])
    return panel