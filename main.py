from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Contacto(BaseModel):
    nombre: str
    telefono: int
    categoria: str

all_contact = []

@app.post('/')
def insertar_contacto(contacto: Contacto):
    all_contact.append(contacto)
    print(all_contact)
    return {"mensaje": f"contacto {contacto.nombre} insertado correctamente"}

@app.get('/')
def mostrar_contacto():
    print(all_contact)
    return [x.model_dump() for x in all_contact]

@app.post('/{contacto_nombre}')
def mostrar_contacto_param(contacto_nombre:str):
    for x in all_contact:
        #Es un objeto por lo que sería x.nombre 
        #Si fuera un dic sería x["nombre"]
        if x.nombre == contacto_nombre:
            return {"Contacto: ": x.nombre}
    return {"Contacto no encontrado"}

@app.delete('/{contacto_nombre}')
def eliminar_contacto(contacto_nombre):
    for x, i in enumerate(all_contact):
        if i.nombre == contacto_nombre:
            all_contact.pop(x)
            return {"Contacto eliminado correctamete"}
    return {"Contacto no encontrado"}

@app.put('/{contacto_nombre}')
def actualizar_contacto(contacto_nombre, updateContact:Contacto ):
    for position, objeto in enumerate(all_contact):
        if objeto.nombre == contacto_nombre:
            #Si el parámetro recibido es correcto, actualizamos los datos 
            objeto.nombre = updateContact.nombre
            all_contact[position] = objeto
            return {"Contacto actualizado correctamente"}
    return {"Contacto no encontrado"}


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)

# http://127.0.0.1:8000 


"""
Para la serielizacion
contactos = [
    Contacto(nombre="Ana",telefono="1232",categoria="Categ"),
    Contacto(nombre="Pepe",telefono="1232",categoria="Categ"),
    Contacto(nombre="Maria",telefono="1232",categoria="Categ"),
]

@app.get('/')
def mostrar_contacto():
    # Búsqueda:   pydantic => serializacion => model_dump
    return [x.model_dump() for x in contactos]
"""