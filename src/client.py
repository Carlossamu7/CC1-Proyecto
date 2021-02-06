"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación del cliente
"""

import requests
import json
import os
from dotenv import load_dotenv

# Variables de entorno
load_dotenv()
PORT = os.getenv('PORT')
CLIENT_HOST = os.getenv('CLIENT_HOST')

# Variables globales
RUTA = "http://" + CLIENT_HOST + ":" + str(PORT)
PARAM = {'content-type': 'application/json'}

#############################
###         Datos         ###
#############################

asignatura = {
    "id": "003",
    "nombre_asignatura": "Armonía",
    "curso": 2,
    "concepto": "Nociones de acordes",
    "profesor": "Valdivia",
    "horario": "V:16-18",
    "aula": "Aula02"
}

asignatura2 = {
    "id": "002",
    "nombre_asignatura": "Coro",
    "curso": 1,
    "concepto": "Nociones básicas acerca de canto",
    "profesor": "Javi",
    "horario": "V:20-21",
    "aula": "Aula03"
}

alumno = {
    "nombre": "Pepe",
    "email": "pepe@gmail.com",
    "dni": "71254236Y",
    "lista_asignaturas" : ["Lenguaje Musical"]
}

#############################
###       Funciones       ###
#############################

def print_request(response):
    print("Código de estado: {}".format(response.status_code))
    print(response.text)

#############################
###  Historias de usuario ###
#############################

# Ruta inicial de bienvenida
print("Ruta iniciial de bienvenida")
print_request(requests.get(RUTA + "/"))
