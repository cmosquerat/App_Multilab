
import os



## Configuraciones
name = "\n"

host = "0.0.0.0"

port = int(os.environ.get("PORT", 4000))

debug = False

contacts = "https://www.multilab.co/"

code = "https://github.com/cmosquerat?tab=repositories"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'

data_mun = "municipios.csv"

data_depto = "departamentos.csv"

geojson_deptos = "colombia.geo.json"

geojson_mun = "municipios_geojson.geojson"

not_elements = {'Unnamed: 0','municipio', 'departamento', 'muestras', "unnamed: 0", "Rango moda ph", "Rango moda n",
 "Rango moda mo","Rango moda k","Rango moda ca", "Rango moda mg", "Rango moda na", "Rango moda al", "Rango moda cic", "Rango moda p"
 ,"Rango moda fe", "Rango moda mn", "Rango moda zn", "Rango moda cu", "Rango moda s", "Rango moda b", "Rango moda ar", "Rango moda l", "Rango moda a","clasificacion" }


rangos = {"Rangos ph","Rangos n","Rangos mo","Rangos k","Rangos ca",
"Rangos mg","Rangos na","Rangos al","Rangos cic","Rangos p","Rangos fe",
"Rangos mn","Rangos zn","Rangos cu","Rangos s","Rangos b","Rangos ar",
"Rangos l","Rangos a"}


elementos = {"ph","n","mo","k","ca","mg","na","al","cic","p","fe","mn","zn","cu","s","b","ar","l","a"}

## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"




