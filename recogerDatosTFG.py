import serial
import os
import time as t
import requests as req

comandos = {"posix": {'puertoSerie' : '/dev/ttyUSB0'},
            "nt": {'puertoSerie' : 'COM3'}}

arduino = serial.Serial(comandos[os.name]["puertoSerie"], 9600)


print("Leyendo datos")

def guardarDatos(texto):
    peticion = req.post('http://localhost:8080/v1/insert', data = texto)
    print(peticion.status_code)
    

while True:
    
    datos = arduino.readline()
    guardarDatos(datos)

    t.sleep(30)