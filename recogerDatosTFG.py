import serial
import os
import time as t

comandos = {"posix": {"ruta": '.', 'puertoSerie' : '/dev/ttyUSB0'},
            "nt": {"ruta": 'D:/Drive/Universidad/4º Cuarto/Segundo semestre/TFG/TFG/Codigo/CodigoPython', 'puertoSerie' : 'COM3'}}

arduino = serial.Serial(comandos[os.name]["puertoSerie"], 9600)

cabecera = comandos[os.name]["ruta"] + "/datos"

print("Guardando en: " + cabecera)

print("Leyendo datos")

def escribirFich(texto, ruta):

    f = open(ruta, "ab")

    if os.stat(ruta).st_size == 0:
        f.write(b"[")
    else:
        f.seek(-1, 2)
        f.truncate()
        f.write(b",")
    f.write(texto)
    f.write(b"]")
    f.close()

while True:

    ruta = cabecera + t.strftime("%m-%d-%Y") + ".json"
    
    datos = arduino.readline()
    escribirFich(datos, ruta)

    t.sleep(30)