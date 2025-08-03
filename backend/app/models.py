from sqlalchemy import Integer, Column, String
from .database import base

class Task(base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, default="")
    