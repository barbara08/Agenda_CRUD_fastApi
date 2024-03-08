# Importamos la clase FastApi del módulo fastapi 
from fastapi import FastAPI

# Para validación de datos usaremos la librería pydantic e importamos BaseModel 
from pydantic import BaseModel
# Este es opcional, es para decir que un atributo puede ser tipo int o str (por ej.)
# Se anotaria sobre el atributo que lo necesite, en este caso lo pondremos en editorial
from typing import Optional

#Instanciamos la clase creando un objeto (app)
app = FastAPI()


# Creamos la class Libro
# Con BaseModel lo que hace es asegurarnos de que cuando ingresemos datos => titulo sea de tipo str
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

# CREMAOS VARIOS ENDPOINTS

    # Creamos función que nos devuelva algo index()
    # Crear la ruta => http://127.0.0.1:8000
    # Poner un decorador => @ para que modificar a la funcion que le sigue, en este caso lo que hace es registrar la función index()
    # Cuando alguien llama a la ruta raiz con la petición get quiere que se ejecute la función 

# 1º Endpoint que nos devuelva algo

@app.get('/')
def index():
    return "hola que tal"

"""
# Cuando se cre un diccionario, fastApi lo convierte directamente en json
def index():
    return {"MENSAJE" : "hola que tal"}
"""

# 2º Endpoint para crer una ruta con parámetros variables
    # Parámeytros variables lo anotamos dentro de {} en la ruta
    # def mostrar_libro(id): => El id lo devuelve como string por lo que habrá que cambiarlo a int (se anota cuando se crea la función)
    # def mostrar_libro(id: int):
    # En el navegador anotar la ruta completa => http://127.0.0.1:8000/libros/3

@app.get('/libros/{id}')
def mostrar_libro(id: int):       
    return {"data": id}   

# 3º Endpoint para crear una ruta con post para insertar datos con la class Libro

@app.post('/libros')
def insertar_libro(libro: Libro):
    return {"mensaje": f"libro {libro.titulo} insertado"}

# En el navegador ejecutamos la ruta http://127.0.0.1:8000/docs
# fatApi crea automáticamente la docs
# Desde aquí se podrá insertar los datos de los libros


# FALTA CONECTARSE A LA BBDD





"""
# Para levantar el sevidor:
    COMANDO
    uvicorn main:app --reload

    main = > nombre archivo principal
    app => nombre de la aplicación
    --reload => el sevidor se mantenga escuchando y no tener que levantar siempre el servidor

    Cuando levantemos el servidor aparacerá en que puerto se encuentra nuestra API
        INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    copiamos la ruta     http://127.0.0.1:8000   y vamos al navegador
"""


