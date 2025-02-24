import streamlit as st
import random 
import requests

from googletrans import Translator

st.set_page_config(
    page_title="Traductor de palabras",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded",
)

UNSPLASH_API_KEY = '1s5UZIfHDW2tbXxvA6IFzq9rsz1Hyl45_aWE0Nkq8FE'

def get_traduccion(palabra_ingles):
    try:
        translator = Translator()
        translation = translator.translate(palabra_ingles, src='es', dest='en')

        return translation.text
    except Exception as e:
        print(f"Error al realizar la traducción: {e}")
        return None
    
def obtener_imagen(palabra):
    url = f"https://api.unsplash.com/search/photos?query={palabra}&client_id={UNSPLASH_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            st.write(f"Error: No se pudo obtener la imagen. Código de estado: {response.status_code}")
        elif not data['results']:
            st.write("No se encontraron imágenes para esa palabra.")
        else:
            
            st.write(f"Aquí tienes una imagen relacionada con la palabra '{palabra}':")
            return data['results'][0]['urls']['regular']
    except Exception as e:
        print(f"Error al obtener la imagen: {e}")
        st.write("Error al realizar la solicitud de imagen.")
        return None

#seteo el título de la app 
st.title("📖 Traductor de palabras Español-Inglés")
st.markdown("Escribe cualquier palabra en español, y descubre su traducción al inglés")

#establezco el input para que el usuario escriba la palabra
palabra_ingles = st.text_input("Escribe una palabra en español", value="")
if palabra_ingles:
    st.write(f"La palabra que escribiste es: {palabra_ingles}")

input_palabra = None

if palabra_ingles:
    input_palabra = get_traduccion(palabra_ingles)

if palabra_ingles:
    input_palabra = get_traduccion(palabra_ingles)

if input_palabra:
    st.write(f"La traducción de {palabra_ingles} al inglés es: {input_palabra}")
    imagen_url = obtener_imagen(palabra_ingles)
    if imagen_url:
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <img src="{imagen_url}" width="600" height="400" style="object-fit: contain;"/>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.write("No se encontró una imagen relacionada.")


