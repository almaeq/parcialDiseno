
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.mutant_service import MutantService
from repositories.dna_repository import get_dna_record, create_dna_record
from models.dna_model import DnaRecord
from pydantic import BaseModel, field_validator 

router = APIRouter()
mutant_service = MutantService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DnaRequest(BaseModel):
    dna: list[str]

    @field_validator("dna")
    def validate_dna(cls, v):
        # Validar si la lista está vacía
        if not v:
            raise HTTPException(status_code=422, detail="DNA sequence cannot be empty.")
        
        # Verificar que todas las cadenas tengan la misma longitud
        length = len(v[0])
        if not all(len(row) == length for row in v):
            raise HTTPException(status_code=422, detail="All DNA rows must be the same length.")
        
        # Validar que solo contenga caracteres válidos
        valid_chars = {"A", "T", "C", "G"}
        if not all(set(row).issubset(valid_chars) for row in v):
            raise HTTPException(status_code=422, detail="DNA sequence contains invalid characters.")
        
        return v

@router.post("/mutant/")
async def detect_mutant(dna_request: DnaRequest, db: Session = Depends(get_db)):
    dna_sequence_str = ','.join(dna_request.dna)
    existing_record = get_dna_record(db, dna_sequence_str)
    
    if existing_record:
        is_mutant = existing_record.is_mutant
    else:
        is_mutant = mutant_service.is_mutant(dna_request.dna)
        create_dna_record(db, dna_sequence_str, is_mutant)

    if is_mutant:
        return {"message": "Mutant detected"}
    else:
        raise HTTPException(status_code=403, detail="Not a mutant")

@router.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    count_mutant_dna = db.query(DnaRecord).filter(DnaRecord.is_mutant == True).count()
    count_human_dna = db.query(DnaRecord).filter(DnaRecord.is_mutant == False).count()
    ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0
    return {
        "count_mutant_dna": count_mutant_dna,
        "count_human_dna": count_human_dna,
        "ratio": ratio
    }
