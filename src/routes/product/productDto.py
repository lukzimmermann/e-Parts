from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PriceDto(BaseModel):
    quantity: float
    price: float

class SupplierProductDto(BaseModel):
    number: str
    product_page: str
    price: Optional[list[PriceDto]] = None

class SupplierDto(BaseModel):
    id: int
    name: str
    product_detail: Optional[SupplierProductDto] = None

class AttributeDto(BaseModel):
    id: int
    parent_id: int | None
    name: str
    numeric_value: float
    text_value: str | None
    unit_id: int
    unit_name: str

class DocumentDto(BaseModel):
    description: str
    type: str
    url: str

class ProductDto(BaseModel):
    id: int
    create_at: datetime
    update_at: datetime
    name: str
    category_id: int
    category_name: str
    manufacture: str
    manufacture_number: str
    minimum_quantity: float
    quantity: Optional[float] = None
    suppliers: Optional[list[SupplierDto]] = None
    attributes: Optional[list[AttributeDto]] = None
    documents: Optional[list[DocumentDto]] = None


