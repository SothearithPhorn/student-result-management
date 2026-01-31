from fastapi import FastAPI
from .database import engine, Base
from .models import Student  # Updated import

# Create all tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Student Result Manager API",
    description="REST API for managing student records and results",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Student Result Manager API",
        "version": "1.0.0",
        "status": "running",
        "tables": ["students"]
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}