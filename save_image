import requests
from PIL import Image
from io import BytesIO
import sys
import os

def obtener_dimensiones_imagen(ruta_imagen):
    # Abrir la imagen
    imagen = Image.open(ruta_imagen)
    
    # Obtener las dimensiones (ancho x alto)
    ancho, alto = imagen.size
    
    # Cerrar la imagen
    imagen.close()

    return ancho, alto

def get_format_from_url(url):
    file_name = os.path.basename(url)
    name, extension = os.path.splitext(file_name)
    image_format = extension[1:]
    return image_format

def descargar_y_guardar_imagen(url, ruta_local):
    response = requests.get(url)
    
    if response.status_code == 200:
        imagen = Image.open(BytesIO(response.content))
        print("\nruta local: " + ruta_local)
        imagen.save(ruta_local)
        print(f'Imagen descargada y guardada en {ruta_local}')
        return ruta_local
    else:
        print(f'Error al descargar la imagen. Código de estado: {response.status_code}')
        return None

url_imagen = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/220px-Logo_of_Twitter.svg.png'


ruta_local = 'imagen_local'+"."+get_format_from_url(url_imagen)
ruta_local_descargada = descargar_y_guardar_imagen(url_imagen, ruta_local)
ancho, alto = obtener_dimensiones_imagen(ruta_local_descargada)
# Imprimir las dimensiones
print(f"Ancho: {ancho}px, Alto: {alto}px")