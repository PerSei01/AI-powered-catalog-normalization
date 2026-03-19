from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)

class SupplierUpdate(BaseModel):
    name: str
    priority: int

class SupplierCreate(BaseModel):
    name: str
    priority: int