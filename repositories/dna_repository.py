from sqlalchemy.orm import Session
from models.dna_model import DnaRecord

class DnaRepository:
    def get_dna_record(self, db: Session, dna_sequence: str):
        return db.query(DnaRecord).filter(DnaRecord.dna_sequence == dna_sequence).first()

    def create_dna_record(self, db: Session, dna_sequence: str, is_mutant: bool):
        db_dna_record = DnaRecord(dna_sequence=dna_sequence, is_mutant=is_mutant)
        db.add(db_dna_record)
        db.commit()
        db.refresh(db_dna_record)
        return db_dna_record