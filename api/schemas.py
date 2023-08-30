from pydantic import BaseModel
from datetime import date


# Carriers
class CarriersBase(BaseModel):
    carrier_name: str
    account_number: str | None


class Carriers(CarriersBase):
    id: int

    class Config:
        from_attributes = True


# Products
class ProductBase(BaseModel):
    product_name: str
    product_description: str | None = None


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


# Bills
class BillsBase(BaseModel):
    carrier_id: int
    product_id: int
    billed_date: date
    bill_due_date: date
    base_charge: float
    ancillary_charge: float
    taxes: float
    credits: float
    paid_date: date | None = None


class Bills(BillsBase):
    id: int
    totals: float
    is_paid: bool

    class Config:
        from_attributes = True


"""
# Our users who can update the database
class UserBase(BaseModel):
    user_name: str
    email: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
"""
