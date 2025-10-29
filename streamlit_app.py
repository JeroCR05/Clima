# aqui va el codigo de la aplicacion principal

# clima.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")
BASE = "https://api.openweathermap.org/data/2.5"

def obtener_clima_actual(ciudad, unidades="metric"):
    # unidades = "metric" (Celsius) o "imperial" (Fahrenheit)
    url = f"{BASE}/weather"
    params = {"q": ciudad, "appid": API_KEY, "units": unidades, "lang": "es"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    ciudad = input("Ciudad: ")
    datos = obtener_clima_actual(ciudad)
    print(datos)
