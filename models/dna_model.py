# models/dna_model.py

from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class DnaRecord(Base):
    __tablename__ = "dna_records"
    id = Column(Integer, primary_key=True, index=True)
    dna_sequence = Column(String, unique=True, nullable=False)
    is_mutant = Column(Boolean, nullable=False)
