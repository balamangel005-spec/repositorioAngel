from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Ejemplo para Render",
    description="Proyecto desde cero para evaluación de FastAPI, Git y Render",
    version="1.0.0"
)

class Item(BaseModel):
    nombre: str
    precio: float
    stock: int

@app.get("/")
def home():
    return {"estado": "activo", "mensaje": "¡Bienvenido a mi API en Render!"}

@app.get("/saludo/{usuario}")
def saludar_usuario(usuario: str, edad: int = None):
    if edad:
        return {"mensaje": f"Hola {usuario}, tienes {edad} años."}
    return {"mensaje": f"¡Hola {usuario}, bienvenido!"}

@app.post("/items/")
def crear_item(item: Item):
    return {
        "mensaje": "Item registrado exitosamente",
        "data": item
    }