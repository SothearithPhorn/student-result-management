# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# PostgreSQL DATABASE URL
DATABASE_URL = "postgresql://postgres:021020@localhost:5432/student_manager_db"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True  # Optional: shows SQL queries in console for debugging
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session in FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
