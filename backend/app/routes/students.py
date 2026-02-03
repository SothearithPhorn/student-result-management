from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Student

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.get("/")
def get_all_students(db: Session = Depends(get_db)):
    """Retrieve all students"""
    students = db.query(Student).all()
    return students

@router.get("/{student_id}",)
def get_student(student_id: int, db: Session = Depends(get_db)):
    """Retrieve a student by ID"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        return {"error": "Student not found"}
    return student