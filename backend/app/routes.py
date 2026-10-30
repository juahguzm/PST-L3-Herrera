from fastapi import APIRouter
from .schemas import LecturaEntrada, ComandoLED
from . import services

router = APIRouter()

@router.get("/salud")
def salud():
    return {"estado": "ok", "laboratorio":3}

@router.get("/lecturas")
def get_lecturas():
    return services.listar_lecturas()

@router.post("/lecturas", status_code=201)
def post_lectura(datos: LecturaEntrada):
    return services.guardar_lectura(datos)

@router.get("/led")
def get_led():
    return services.consultar_led()

@router.put("/led")
def put_led(comando: ComandoLED):
    return services.cambiar_led(comando)

from fastapi import APIRouter, Query
from app.services import calcular_promedio_lecturas

# ... (tus otras rutas existentes) ...

@router.get("/lecturas/promedio")
def obtener_promedio(
    n: int = Query(default=3, ge=1, le=100, description="Número de últimas lecturas a promediar")
):
    return calcular_promedio_lecturas(n)