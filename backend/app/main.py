from fastapi import FastAPI
from .database import engine, Base
from .models import Student  # Updated import
from .routes import students_router  # Updated import


# Create FastAPI app
app = FastAPI(
    title="Student Result Manager API",
    description="REST API for managing student records and results",
    version="1.0.0"
)

# Create all tables
Base.metadata.create_all(bind=engine)


# Include routers
app.include_router(students_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Student Result Manager API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "students": "/api/students",
            "docs": "/docs",
        }
       
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}