from pydantic import BaseModel, Field, field_validator

class SupplierUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    priority: int = Field(..., ge=0)

    @field_validator("name")
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty or whitespace")

        return value

class SupplierCreate(BaseModel):
    name: str = Field(..., min_length=1)
    priority: int = Field(..., ge=0)

    @field_validator("name")
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty or whitespace")

        return value
    
class SupplierResponse(BaseModel):
    id: int
    name: str
    priority: int

    class Config:
        from_attributes = True

class SupplierPatch(BaseModel):
    name: str | None = Field(None, min_length=1)
    priority: int | None = Field(None, ge=0)

    @field_validator("name")
    def validate_name(cls, value):
        if value is None:
            return value

        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty or whitespace")

        return value