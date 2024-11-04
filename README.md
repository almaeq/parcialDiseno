# Detector e mutantes

## Descripción

El proyecto consiste en un servicio web que recibe una secuencia de ADN y determina si es mutante o no. La secuencia de ADN se recibe como una lista de cadenas de caracteres, cada una de las cuales representa una fila de la ADN. El servicio debe tener una ruta POST que reciba la secuencia de ADN y devuelva un mensaje indicando si la secuencia es mutante o no.

## Requisitos

- Se debe utilizar una base de datos relacional para almacenar los datos de las secuencias de ADN.
- Se debe utilizar la biblioteca FastAPI para crear el servicio web.
- Se debe utilizar la biblioteca SQLAlchemy para interactuar con la base de datos.
- Se debe utilizar la biblioteca Pydantic para validar los datos recibidos en la ruta POST.
- Se debe utilizar la biblioteca pytest para escribir los tests unitarios.

## Estructura del proyecto

- El directorio `config` contiene los archivos de configuración para la base de datos y la conexión a la base de datos.
- El directorio `controllers` contiene los archivos de controladores para la ruta POST.
- El directorio `models` contiene los archivos de modelos para la base de datos.
- El directorio `repositories` contiene los archivos de repositorios para la base de datos.
- El directorio `services` contiene los archivos de servicios para la detección de mutantes.
- El archivo `main.py` es el archivo principal del proyecto.
- El archivo `test_mutant_controller.py` contiene los tests unitarios para la ruta POST.

## Ejecución del proyecto

Para ejecutar el proyecto, sigue los siguientes pasos:

1. Abra una terminal y navega hasta el directorio del proyecto.
2. Ejecuta el siguiente comando para instalar las dependencias del proyecto: `pip install -r requirements.txt`.
3. Ejecuta el siguiente comando para crear la base de datos: `python main.py db create`.
4. Ejecuta el siguiente comando para inicializar la base de datos: `python main.py db init`.
5. Ejecuta el siguiente comando para iniciar el servidor web: `python main.py run`.
6. Abre una segunda terminal y navega hasta el directorio del proyecto.
7. Ejecuta el siguiente comando para ejecutar los tests unitarios: `pytest`.

## Ejemplo de uso

Para ejecutar el servicio web, sigue los siguientes pasos:

1. Abre una terminal y navega hasta el directorio del proyecto.
2. Ejecuta el siguiente comando para iniciar el servidor web: `python main.py run`.
3. Abre una segunda terminal y navega hasta el directorio del proyecto.
4. Ejecuta el siguiente comando para enviar una solicitud POST a la ruta `/mutant/` con una secuencia de ADN: `curl -X POST http://localhost:8000/mutant/ -H "Content-Type: application/json" -d '{"dna": ["ATCG", "ATCG", "ATCG", "ATCG"]}'`.
5. Espera a que se complete la solicitud y vea el resultado en la terminal.

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
