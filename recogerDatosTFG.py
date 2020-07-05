import serial
import os
import time as t
import requests as req
import json

comandos = {"posix": {'puertoSerie' : '/dev/ttyUSB0'},
            "nt": {'puertoSerie' : 'COM3'}}

arduino = serial.Serial(comandos[os.name]["puertoSerie"], 9600)


print("Leyendo datos")

def guardarDatos(datos):
    jsonData = json.loads(datos)
    peticion = req.post('http://localhost:8080/v1/insert', json=jsonData)
    print(peticion.status_code)
    

while True:
    
    datos = arduino.readline()
    guardarDatos(datos.decode("utf-8") )

    t.sleep(30)