from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Boolean  # Явный импорт

db = SQLAlchemy()

class Task(db.Model):
    id = Column(Integer, primary_key=True)  # Должно работать с автодополнением
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False)
