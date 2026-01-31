"""
Student Model
Represents the students table in the database
"""

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base


class Student(Base):
    """
    Student model - stores student information
    
    Attributes:
        id: Unique identifier (primary key)
        name: Student's full name (required)
        email: Student's email address (optional, unique)
        phone: Student's phone number (optional)
        created_at: Timestamp when student was added
    """
    __tablename__ = "students"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Student information
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        """String representation of Student"""
        return f"<Student(id={self.id}, name='{self.name}')>"