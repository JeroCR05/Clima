import os, requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OWM_API_KEY") or os.getenv("API_KEY")
print("API_KEY encontrada?:", bool(API_KEY))

ciudad = "Medellin,CO"
url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}

r = requests.get(url, params=params, timeout=10)
print("Status code:", r.status_code)
print("Respuesta (json):", r.json())
