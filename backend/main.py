from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import engine, get_db
from models import Base, Supplier
import models
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

suppliers = [
    {"id": 1, "name": "Nike Supplier", "priority": 1},
    {"id": 2, "name": "Adidas Supplier", "priority": 2},
    {"id": 3, "name": "Puma Supplier", "priority": 3},
]
class SupplierCreate(BaseModel):
    name: str
    priority: int

@app.get("/")
def read_root():
    return {"message": "Hello from Catalog AI backend"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/suppliers")
def get_suppliers(db: Session = Depends(get_db)):
    suppliers = db.query(Supplier).all()
    return suppliers

@app.post("/suppliers")
def create_supplier(name: str, priority: int, db: Session = Depends(get_db)):

    supplier = Supplier(
        name=name,
        priority=priority
    )

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier