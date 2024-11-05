from fastapi import FastAPI
from controllers.mutant_controller import router as mutant_router

# Instancia de FastAPI
app = FastAPI()

# Registrar las rutas del controlador
app.include_router(mutant_router)
