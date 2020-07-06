import serial
import os
import time as t
import requests as req
import json
import re

comandos = {"posix": {'puertoSerie' : '/dev/ttyUSB0'},
            "nt": {'puertoSerie' : 'COM3'}}

arduino = serial.Serial(comandos[os.name]["puertoSerie"], 9600)


print("Leyendo datos")

def guardarDatos(datos):
    jsonData = json.loads(datos)
    try:
        peticion = req.post('http://localhost:8080/v1/insert', json=jsonData)
        
    except req.exceptions.Timeout:
        print("Maybe set up for a retry, or continue in a retry loop")
    except req.exceptions.TooManyRedirects:
        print("Tell the user their URL was bad and try a different one")
    except req.exceptions.RequestException as e:
        print(e.args)
    
    
    
    
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError:
        return False
    return True

while True:
    
    datos = arduino.readline()

    if validateJSON(datos):
        guardarDatos(datos.decode("utf-8"))

    t.sleep(30)