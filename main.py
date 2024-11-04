from fastapi import FastAPI
from controllers import mutant_controller
from config.database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar los routers
app.include_router(mutant_controller.router)
