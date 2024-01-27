#API: APPLICATION programing interface
#nasa Api:https://api.nasa.gov/
#api_Key_NASA   GA9scJf2nHfCL5dwpL850fs61L2CwAniFksteKH9
#developer Jaime C
#Date 24012024
#script description: get data from NASA API about comets

import requests

def get_comet_data(api_key):
    print(":::comet information :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo3726712?api_key={api_key}"

    try:
        #Realizar la solicitud a la API
        response = requests.get(url)
        response.raise_for_status() #=> Valida si se presenta algún error en la petición
        #Convertir la respuesta a formato JSON (JS Object Notation)
        datos = response.json()

        print(f"Comet name: {datos['name']}")
        print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición a la API de NASA: {e}") 
      
    api_Key_NASA = 'GA9scJf2nHfCL5dwpL850fs61L2CwAniFksteKH9'
    get_comet_data(api_Key_NASA)

