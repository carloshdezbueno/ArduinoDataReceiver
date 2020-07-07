import time as t

import requests as req

print("Enviando peticiones")

def enviarPeticion():
    
    try:
        req.post('http://localhost:8080/v1/insert')
        
    except req.exceptions.Timeout:
        print("Maybe set up for a retry, or continue in a retry loop")
    except req.exceptions.TooManyRedirects:
        print("Tell the user their URL was bad and try a different one")
    except req.exceptions.RequestException as e:
        print(e.args)

while True:

    enviarPeticion()

    t.sleep(30)
