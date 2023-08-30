from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base


# Carrier table
class Carrier(Base):
    __tablename__ = "carrier"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    carrier_name = Column(String, unique=False, index=True)
    account_number = Column(String, unique=False, index=True)


# Products table
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String, unique=False, index=True)
    product_description = Column(String, unique=False, index=False)


# Bill table
class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    carrier_id = Column(Integer, ForeignKey("carrier.id"), index=True)
    billed_date = Column(DateTime, index=True)
    bill_due_date = Column(DateTime, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), index=True)
    base_charge = Column(Float, default=0)
    ancillary_charge = Column(Float, default=0)
    taxes = Column(Float, default=0)
    credits = Column(Float, default=0)
    totals = Column(Float, default=0)
    paid_date = Column(DateTime)
    is_paid = Column(Boolean, default=False)
