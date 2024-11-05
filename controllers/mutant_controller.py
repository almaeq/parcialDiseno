from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import Database
from services.mutant_service import MutantService
from repositories.dna_repository import DnaRepository
from models.dna_model import DnaRecord
from pydantic import BaseModel, field_validator

database = Database()
mutant_service = MutantService()
dna_repository = DnaRepository()

router = APIRouter()

class DnaRequest(BaseModel):
    dna: list[str]

    @field_validator("dna")
    def validate_dna(cls, v):
        if not v:
            raise HTTPException(status_code=422, detail="DNA sequence cannot be empty.")
        
        length = len(v[0])
        if not all(len(row) == length for row in v):
            raise HTTPException(status_code=422, detail="All DNA rows must be the same length.")
        
        valid_chars = {"A", "T", "C", "G"}
        if not all(set(row).issubset(valid_chars) for row in v):
            raise HTTPException(status_code=422, detail="DNA sequence contains invalid characters.")
        
        return v

# Dependencia de la sesión de base de datos
def get_db():
    db = database.get_session()
    try:
        yield db
    finally:
        db.close()

@router.post("/mutant/")
async def detect_mutant(dna_request: DnaRequest, db: Session = Depends(get_db)):
    dna_sequence_str = ','.join(dna_request.dna)
    existing_record = dna_repository.get_dna_record(db, dna_sequence_str)
    
    if existing_record:
        is_mutant = existing_record.is_mutant
    else:
        is_mutant = mutant_service.is_mutant(dna_request.dna)
        dna_repository.create_dna_record(db, dna_sequence_str, is_mutant)

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