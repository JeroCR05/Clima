# aqui va el codigo de la aplicacion principal

# importar las librerías necesarias
import streamlit as st
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# Título de la app
st.title("🌦️ App del Clima en Colombia")
st.write("Consulta el clima actual de tu ciudad con datos en tiempo real 🌍")

# Campo de entrada
ciudad = st.text_input("Ingresa el nombre de la ciudad:", "Medellín")

# Obtener API key desde variable de entorno
api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    st.error("⚠️ No se encontró la API Key. Asegúrate de haber configurado OPENWEATHER_API_KEY en tu entorno.")
else:
    if st.button("Consultar clima"):
        if ciudad:
            try:
                # URL de la API (usa unidades métricas y español)
                url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"

                # Llamado a la API
                respuesta = requests.get(url)
                datos = respuesta.json()

                # Mostrar la respuesta cruda (para depuración opcional)
                # st.write(datos)

                if respuesta.status_code == 200 and "main" in datos:
                    st.success(f"✅ Ciudad encontrada: {datos['name']}, {datos['sys']['country']}")

                    # Mostrar la info del clima
                    temp = datos['main']['temp']
                    desc = datos['weather'][0]['description'].capitalize()
                    humedad = datos['main']['humidity']
                    viento = datos['wind']['speed']
                    presion = datos['main']['pressure']

                    st.metric(label="🌡️ Temperatura", value=f"{temp} °C")
                    st.metric(label="💧 Humedad", value=f"{humedad}%")
                    st.metric(label="🌬️ Viento", value=f"{viento} m/s")
                    st.metric(label="⚖️ Presión", value=f"{presion} hPa")

                    st.write(f"**Descripción:** {desc}")
                    st.write(f"📅 Datos actualizados: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                else:
                    mensaje = datos.get("message", "No se pudo obtener el clima.")
                    st.error(f"⚠️ No se encontró la ciudad '{ciudad}'. Detalle: {mensaje}")

            except Exception as e:
                st.error(f"❌ Error al consultar la API: {e}")

        else:
            st.warning("⚠️ Por favor, ingresa una ciudad antes de consultar.")




