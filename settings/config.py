
import os



## Configuraciones
name = "Multilab Agroanalítica"

host = "192.168.101.48"

port = int(os.environ.get("PORT", 5000))

debug = False

contacts = "https://www.multilab.co/"

code = "https://github.com/cmosquerat?tab=repositories"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'

data = "tabla.xlsx"

geojson = "colombia.geo.json"

not_elements = {"Unnamed: 0",'municipio', 'departamento'}


## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"



