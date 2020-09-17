import time as t

import requests as req
import datetime as dt

print("Enviando peticiones")

def enviarPeticion():
    
    try:
        req.post('http://localhost:8080/v1/grabData')
        
    except req.exceptions.Timeout:
        print("Maybe set up for a retry, or continue in a retry loop")
    except req.exceptions.TooManyRedirects:
        print("Tell the user their URL was bad and try a different one")
    except req.exceptions.RequestException as e:
        print(e.args)

while True:

    enviarPeticion()

    #Se ejecuta cada 10 minutos
    t.sleep(120)
