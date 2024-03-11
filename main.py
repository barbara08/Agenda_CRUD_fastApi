from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Contacto(BaseModel):
    nombre: str
    telefono: int
    categoria: str

contactos = [
    Contacto(nombre="Ana",telefono="1232",categoria="Categ"),
    Contacto(nombre="Pepe",telefono="1232",categoria="Categ"),
]

@app.post('/')
def insertar_contacto(contacto: Contacto):
    return {"mensaje": f"contacto {contacto.nombre} insertado correctamente"}

@app.get('/')
def mostrar_contacto():
    # Búsqueda:   pydantic => serializacion => model_dump
    return [x.model_dump() for x in contactos]


