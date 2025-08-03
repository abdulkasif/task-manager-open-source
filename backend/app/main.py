from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

models.base.metadata.create_all(bind=database.engine)

# Dependency to get db session
def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_roots():
    return {"message":"Welcome to Task Manager API"}