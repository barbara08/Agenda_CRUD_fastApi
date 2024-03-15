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

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)




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