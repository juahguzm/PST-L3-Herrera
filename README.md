# Lab 3 Estructura de un backend
# Juan Miguel Herrera Guzmán
# Objetivos de la práctica
●	Identificar la entrada de la aplicación, las rutas, los modelos, la lógica y el almacenamiento.
●	Ejecutar la API localmente y probar sus cinco endpoints desde Swagger.
●	Conectar el ESP8266 con el backend y comprobar el cambio del LED.
●	Agregar un endpoint y publicar su trabajo en su repositorio de GitHub.

# Pregunta 1: ¿Qué función recibe el JSON y cuál lo guarda?
Recibe POST, para archivar, guardar o registrar los cambios que realicemos, como cambiar color, humedad, etc.

# Pregunta 2: ¿Qué archivo cambiarías para añadir una URL?
Se agregaría un nuevo boque de código como este, 
@router.get("/nueva-url")
def nueva_funcion():
    return {"mensaje": "Esta es una nueva URL"}

# Pregunta 3: ¿Qué ocurre con las lecturas y el color cuando se reinicia la API? ¿Por qué?
Cuando se reinicia la API, las lecturas se borran debido a que estas no se guardan al no haber una base de datos que permita almacenar los datos. Un ejemplo de esto fue que los datos que pusimos, al reiniciarse, se borraron y mostraron un JSON vacío o en blanco

# Pregunta 4: ¿Por qué una petición con JSON bien escrito puede devolver 422? Indica qué archivo define esa validación.
Una petición con un JSON bien escrito no determina un éxito si el valor o el dato que se escriba no pasa la validación. Un ejemplo de esto fue cuando se dio la humedad un valor de 150, lo cual estaba fuera del rango válido que era de 100 por lo cual, el JSON estaba bien escrito pero el dato no estaba en el rango permitido y por eso arrojaba un valor de 422.

# Pregunta 5: Explica el recorrido completo de una lectura: ESP8266, ruta, modelo, servicio, almacenamiento y respuesta. ¿En qué momento cambia el LED?
a.	ESP8266: Envía los datos del sensor (humedad y temperatura) mediante una petición HTTP POST en formato JSON al servidor. 
b.	Ruta (routes.py): El decorador @ router.post (“/lecturas”) recibe la petición y la dirige a la función correspondiente. 
c.	Modelo: Pydantic valida automáticamente que los campos y rangos del JSON sean correctos; si falla, devuelve un error 422. 
d.	Servicio (services.py): La lógica procesa los datos válidos y los vincula con el estado actual del sistema. 
e.	Almacenamiento (store.py): Guarda la nueva lectura dentro de la lista de memoria del servidor. 
f.	Respuesta: El servidor responde al ESP8266 con un código 201 Created y un JSON que incluye la nueva lectura y el color asignado para el LED.



Código base del curso para leer, ejecutar y modificar a mano, sin IA.
Hardware de referencia: NodeMCU ESP8266, DHT11 y LED RGB de cátodo común.
Este proyecto es una propuesta de material base para acompañar la guía.

## Backend en Windows
Desde backend, en una terminal Command Prompt de VS Code:
```
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Swagger: http://127.0.0.1:8000/docs
En macOS/Linux: python3 -m venv .venv y usar .venv/bin/python.
Los cinco endpoints base están en app/routes.py. La lista guarda como máximo
100 lecturas en memoria y se pierde al reiniciar. Ejecutar un solo proceso.
POST /lecturas retorna HTTP 201 con {"lectura": {...}, "led": "apagado"}.
PUT /led acepta rojo, verde, azul o apagado. No hay autenticación:
utilizar únicamente en la red de laboratorio autorizada.

## Parte 5: Modificar el backend a mano:
Para esta parte de la práctica, se procedió a modificar el archivo backend/app/routes.py,
en donde se actualizó la función que maneja la ruta salud para que el JSON
retornado incluya un nuevo campo "laboratorio": 3 conservando el campo de 
estado. 


## Firmware
Abrir firmware con PlatformIO IDE en VS Code. Copiar include/config.example.h
a include/config.h y completar WiFi, URL con IPv4 del PC e identificador.
Build, Upload y Monitor a 115200 baudios. El ESP envía cada 5 segundos y aplica
el color devuelto por POST /lecturas; PUT /led se refleja en el próximo envío.
Conexiones y pruebas: ver guía. Las dependencias se descargan la primera vez.
No publicar config.h, contraseñas ni tokens.

## Reto
Implementar GET /lecturas/promedio?n=3 a mano; no se incluye la solución.
Devolver cantidad, temperatura_promedio y humedad_promedio (dos decimales).
Validar n de 1 a 100; sin lecturas responder 404; si hay menos de n, usar todas.

## Antes de la sesión
El docente debe probar el firmware en el hardware real y la red del aula,
precargar las herramientas y validar las dependencias en los equipos.
La guía destina 105 minutos a trabajar con el entorno ya preparado.
