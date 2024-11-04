import pytest
from fastapi.testclient import TestClient
from main import app
from config.database import SessionLocal, Base, engine
from models.dna_model import DnaRecord
from sqlalchemy.orm import Session

client = TestClient(app)

# Configura la base de datos para pruebas
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)  # Crear las tablas
    yield
    Base.metadata.drop_all(bind=engine)    # Limpiar después de las pruebas

@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.query(DnaRecord).delete()  # Limpiar registros después de cada prueba
    db.commit()
    db.close()

def test_detect_mutant(db_session):
    response = client.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}

def test_detect_human(db_session):
    response = client.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGACGG", "TCCCTA", "TCACTG"]})
    assert response.status_code == 403
    assert response.json() == {"detail": "Not a mutant"}

def test_invalid_dna_format(db_session):
    response = client.post("/mutant/", json={"dna": ["ATGCGA", "CAGTG", "TTATGT", "AGAAGG", "CCCCTA"]})  # No es NxN
    assert response.status_code == 422  # FastAPI debería devolver un error de validación

def test_invalid_characters_in_dna(db_session):
    response = client.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCXTA", "TCACTG"]})  # X no es válido
    assert response.status_code == 422  # FastAPI debería devolver un error de validación

def test_empty_dna(db_session):
    response = client.post("/mutant/", json={"dna": []})
    assert response.status_code == 422  # Error de validación para secuencia vacía

def test_stats_with_data(db_session):
    # Insertar datos en la base de datos para probar estadísticas
    db_session.add(DnaRecord(dna_sequence="ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG", is_mutant=True))
    db_session.add(DnaRecord(dna_sequence="ATGCGA,CAGTGC,TTATGT,AGACGG,TCCCTA,TCACTG", is_mutant=False))
    db_session.commit()

    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["count_mutant_dna"] == 1
    assert data["count_human_dna"] == 1
    assert data["ratio"] == 1.0  # 1 mutante / 1 humano

def test_stats_empty(db_session):
    # Probar estadísticas cuando no hay datos en la base de datos
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["count_mutant_dna"] == 0
    assert data["count_human_dna"] == 0
    assert data["ratio"] == 0
