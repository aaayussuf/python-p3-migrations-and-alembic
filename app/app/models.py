# models.py

from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, Integer, String, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

# Create database engine
engine = create_engine('sqlite:///migrations_test.db')

# Define Base class
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12')
    )

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: {self.name}, Grade {self.grade}"
