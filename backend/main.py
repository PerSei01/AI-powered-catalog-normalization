from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from database import engine, get_db
from models import Base, Supplier, SupplierUpdate
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
def create_supplier(supplier_data: SupplierCreate, db: Session = Depends(get_db)):

    supplier = Supplier(
    name=supplier_data.name,
    priority=supplier_data.priority
)

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier

@app.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return supplier

@app.delete("/suppliers/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    db.delete(supplier)
    db.commit()

    return {"message": "Supplier deleted successfully"}

@app.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: int, supplier_data: SupplierUpdate, db: Session = Depends(get_db)):

    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    supplier.name = supplier_data.name
    supplier.priority = supplier_data.priority

    db.commit()
    db.refresh(supplier)

    return supplier