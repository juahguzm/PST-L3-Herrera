from . import store
from .schemas import LecturaEntrada, ComandoLED

def guardar_lectura(datos: LecturaEntrada) -> dict:
    lectura = datos.model_dump()
    store.lecturas.append(lectura)
    # Conservamos como máximo las últimas 100 lecturas recibidas.
    del store.lecturas[:-100]
    return {"lectura": lectura, "led": store.estado_led["color"]}

def listar_lecturas() -> list[dict]:
    return store.lecturas

def consultar_led() -> dict:
    return store.estado_led

def cambiar_led(comando: ComandoLED) -> dict:
    store.estado_led["color"] = comando.color
    return store.estado_led

from fastapi import HTTPException
from app.store import store

def calcular_promedio_lecturas(n: int):
    # Si no hay lecturas, devuelve un error 404
    if not store.lecturas:
        raise HTTPException(
            status_code=404, 
            detail="No hay lecturas registradas para calcular el promedio."
        )
    
    # Tomar las últimas n lecturas de la lista
    ultimas_lecturas = store.lecturas[-n:]
    cantidad_real = len(ultimas_lecturas)
    
    # Calcular promedios
    suma_temp = sum(l.temperatura for l in ultimas_lecturas)
    suma_hum = sum(l.humedad for l in ultimas_lecturas)
    
    return {
        "cantidad": cantidad_real,
        "temperatura_promedio": round(suma_temp / cantidad_real, 2),
        "humedad_promedio": round(suma_hum / cantidad_real, 2)
    }