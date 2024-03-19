from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Contact(BaseModel):
    name: str
    telephone: int
    category: str

all_contact = []

# http://127.0.0.1:8000/docs

@app.post('/')
def insert_contact(contact: Contact):
    all_contact.append(contact)
    print(all_contact)
    return {"message": f"contact {contact.name} insert correctly"}

@app.get('/')
def show_contact():
    print(all_contact)
    return [x.model_dump() for x in all_contact]

@app.post('/{contact_name}')
def show_contact_param(contact_name:str):
    for x in all_contact:
        if x.name == contact_name:
            return {"Contact: ": x.name}
    return {"contact not found"}

@app.delete('/{contact_name}')
def delete_contact(contact_name):
    for position, item in enumerate(all_contact):
        if item.name == contact_name:
            all_contact.pop(position)
            return {"contact deleted successfully"}
    return {"contact not found"}

@app.put('/{contact_name}')
def update_contact(contact_name, updateContact:Contact):
    for position, obj in enumerate(all_contact):
        if obj.name == contact_name:
            obj.name = updateContact.name
            obj.telephone = updateContact.telephone
            obj.category = updateContact.category
            all_contact[position] = obj
            return {"contact updated successfully"}
    return {"contact not found"}

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

"""
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

"""