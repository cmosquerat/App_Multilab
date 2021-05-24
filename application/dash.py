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

df_means = data.multilab_preprocess_means()

df_samples = data.preprocess_samples()

geojson = data.geojson

result = Result(df_samples,df_means,geojson)

n_muestras = len(data.df.index)
n_deptos = len(df_means.index)
n_mun = data.df["municipio"].nunique()



# App Instance
app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.PULSE, config.fontawesome])
app.title = config.name



# Navbar
navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
    dbc.NavItem(html.Div([
        dbc.NavLink("Acerca de", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("Prueba de dashboard"), dbc.PopoverBody(about.txt)
        ])
    ])),
    ## links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"), "  Contacts"], href=config.contacts, target="_blank"), 
        dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank")
    ])
])



# Input
inputs = dbc.FormGroup([
    html.H4("Seleccionar Elemento"),
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
            dbc.Col(html.H4("Gráficas Georreferenciadas"), width={"size":6,"offset":3}), 
            dbc.Tabs(className="nav nav-pills", children=
            [
                dbc.Tab(label="Elemento Químico", tab_id="tab-1"),
                dbc.Tab(label="Muestras", tab_id="tab-2"),
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



# Python function to plot total cases
@app.callback(output=Output("plot-total","figure"), inputs=[Input("country","value")]) 
def plot_total_cases(country):
    return result.plot_element(country)



# Python function to plot active cases
@app.callback(output=Output("plot-active","figure"), inputs=[Input("country","value")])
def plot_active_cases(country):
    return result.plot_total()
    

    
# Python function to render output panel
@app.callback(output=Output("output-panel","children"), inputs=[Input("country","value")])
def render_output_panel(country):
    panel = html.Div([
        html.H4("Alcance de Multilab"),
        dbc.Card(body=True, className="text-white bg-primary", children=[
            
            html.H6("Total muestras procesadas", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_muestras), style={"color":"white"}),
            
            html.H6("Número de departamentos en los que se tiene presencia", className="text-danger"),
            html.H3("{:,.0f}".format(n_deptos), className="text-danger"),
            
            html.H6("Número de municipios en los que se tiene presencia", style={"color":"white"}),
            html.H3("{:,.0f}".format(n_mun), style={"color":"white"}),
        
        ])
    ])
    return panel