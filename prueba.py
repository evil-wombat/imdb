import requests

direccion = 'http://www.omdbapi.com/?apikey=f9f8c5d9&i=tt3896198'


respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
else:
    print ('Se ha producido un error', respuesta.status)
