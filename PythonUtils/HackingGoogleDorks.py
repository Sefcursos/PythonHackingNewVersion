
import requests

# Constantes para configurar la API de búsqueda personaliza
API_KEY_GOOGLE = "AIzaSyDkMrOHobXQx4u-lPvtr7T5cPQ-S0Oya-E"
SEARCH_ENGINE_ID = "f23bd4f9471f44b4d"

# Configuración de la consulta y parametros de busqueda
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
page = 1
lang = "lang_es"

# Construcción de la URL para la API de Google Custom Search
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY_GOOGLE}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"

# Realizar la solicitud HTTP GET y convertir la respuesta en JSON
response = requests.get(url)
data = response.json()

# Recuperar la lista de resultados de la respuesta
results = data.get("items", []) # Uso de get para evitar KeyError

for result in results:
    print("\n-------------- Nuevo Resultado --------------")
    print(f"Título: {result.get('title')}")
    print(f"Descripción: {result.get('snippet')}")
    print(f"Enlace: {result.get('link')}")
    print("-----------------------------------------------")