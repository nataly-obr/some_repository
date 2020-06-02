#student.py
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

class Student(Base):
    __tablename__ = 'student'
    
    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100))
    family_name = db.Column('family_name', db.String(100))
    phone_number = db.Column('phone_number', db.String(15), unique = True)
    total_credits = db.Column('total_credits', db.Integer)
    __table_args__ = (db.UniqueConstraint('first_name', 'family_name', name='full_name'),)
