from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

models.base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/tasks")
def create_task(title: str, description: str = "", db: Session = Depends(get_db)):
    task = models.Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/")
def read_roots():
    return {"message":"Welcome to Task Manager API"}