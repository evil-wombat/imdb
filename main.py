import requests

pelicula = input ('Título de la película: ')

API_KEY = 'f9f8c5d9'

direccion_search = "http://www.omdbapi.com/?apikey={}&s={}"
direccion_id = "http://www.omdbapi.com/?apikey={}&i={}"

def peticion (url):
    respuesta = requests.get (url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos ['Response'] == 'False':
            print (datos['Error'])
        else:
            return datos
    else:
        print ('Error en la consulta por id', respuesta.status_code)


respuesta = peticion (direccion_search.format(API_KEY, pelicula)) 
if respuesta is not None:
    peli_1 = respuesta['Search'][0]
    clave = peli_1 ['imdbID']

    respuesta = peticion (direccion_id.format(API_KEY, clave))
    if respuesta is not None:
        titulo = respuesta ['Title']
        year = respuesta ['Year']
        director = respuesta ['Director']
        print ('La peli {}, estrenada en el año {}, está dirigida por {}'.format (titulo, year, director))


"""
if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos ['Response'] == 'False':
        print (datos['Error'])
    else:
        peli_1 = datos['Search'][0]
        clave = peli_1['imdbID']

        direccion_2 = "http://www.omdbapi.com/?apikey={}&i={}".format (API_KEY, clave)
        nueva_respuesta = requests.get (direccion_2)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos ['Response'] == 'False':
                print (datos['Error'])
            else:
                titulo = datos['Title']
                year = datos ['Year']
                director = datos ['Director']
                print ('La peli {}, estrenada en el año {}, está dirigida por {}'.format (titulo, year, director))
        else:
            print ('Error en la consulta por id', nueva_respuesta.status_code)
else:
    print ('Error en búsqueda', respuesta.status_code)
"""