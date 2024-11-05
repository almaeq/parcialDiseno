# Detector de mutantes

## Descripción

El proyecto consiste en un servicio web que recibe una secuencia de ADN y determina si es mutante o no. La secuencia de ADN se recibe como una lista de cadenas de caracteres, cada una de las cuales representa una fila de la ADN. El servicio debe tener una ruta POST que reciba la secuencia de ADN y devuelva un mensaje indicando si la secuencia es mutante o no.

## Requisitos

- Se debe utilizar una base de datos relacional para almacenar los datos de las secuencias de ADN.
- Se debe utilizar la biblioteca FastAPI para crear el servicio web.
- Se debe utilizar la biblioteca SQLAlchemy para interactuar con la base de datos.
- Se debe utilizar la biblioteca Pydantic para validar los datos recibidos en la ruta POST.
- Se debe utilizar la biblioteca pytest para escribir los tests unitarios.

## Ejecución del proyecto

Para ejecutar el proyecto, sigue los siguientes pasos:

1. Abra una terminal y navega hasta el directorio del proyecto.
2.Ejecuta el siguiente comando para crear un entorno virtual: `python3 -m venv env`.
3. Ejecuta el siguiente comando para instalar las dependencias del proyecto: `pip install -r requirements.txt`.
4. Ejecuta el siguiente comando para inicializar el programa: `python3 main.py`.
5. Abrir postman e importar el archivo `mutant_api.postman_collection.json`.
6.En Postman, selecciona el request POST para enviar una secuencia de ADN y verifica si es mutante. Ingresa una secuencia de dna en el cuerpo de la solicitud y envíala.
7.Para obtener estadísticas, selecciona el request GET en Postman para ver el número de mutantes y no mutantes registrados en la base de datos.

Postman se ejecutara en esta URL: http://127.0.0.1:5000/

Como está dockerizado y hosteado en Render también se puede ejecutar en la siguiente URL:https://parcialdiseno.onrender.com

### Para hacer el POST:
 https://parcialdiseno.onrender.com/mutant

 ### Para hacer el GET:
 https://parcialdiseno.onrender.com/stats

## Para ejecutar los tests:
1. Abre una segunda terminal y navega hasta el directorio del proyecto.
2. Ejecuta el siguiente comando para ejecutar los tests: `PYTHONPATH=. pytest --cov=. --cov-report=term-missing `.

## Ejemplo de solicitud POST
```json
{
  "dna": [
    "ATCG",
    "ATCG",
    "ATCG",
    "ATCG"
  ]
}
```
