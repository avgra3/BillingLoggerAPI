"""
TODO:
- Update Bills
- Update Carriers
- Update Products
"""

from sqlalchemy.orm import Session

# from .
import models, schemas
from datetime import date
from datetime import datetime


# Convert string date to date
def convert_date(raw_date: str | None, format: str = "%Y-%m-%d"):
    if isinstance(raw_date, date):
        return raw_date
    if isinstance(raw_date, str):
        return datetime.strptime(raw_date, format).date()
    return None


# Bills
def get_bill(db: Session, bill_id: int):
    return db.query(models.Bill).filter(models.Bill.id == bill_id).first()


def get_bills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bill).offset(skip).limit(limit).all()


def create_bill(db: Session, bill: schemas.BillsBase):
    total_billed = bill.base_charge + bill.ancillary_charge + bill.taxes + bill.credits

    bill_paid = False
    if bill.paid_date:
        bill_paid = True

    billed_date_coverted = convert_date(bill.billed_date)
    bill_due_date_converted = convert_date(bill.bill_due_date)
    if bill.paid_date:
        paid_date = convert_date(bill.paid_date)
    else:
        paid_date = None

    db_bill = models.Bill(
        carrier_id=bill.carrier_id,
        product_id=bill.product_id,
        base_charge=bill.base_charge,
        ancillary_charge=bill.ancillary_charge,
        taxes=bill.taxes,
        credits=bill.credits,
        totals=total_billed,
        is_paid=bill_paid,
        billed_date=billed_date_coverted,
        bill_due_date=bill_due_date_converted,
        paid_date=paid_date,
    )
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill


def get_bill_by_details(
    db: Session, carrier_id: int, billed_date: date, due_date: date
):
    return (
        db.query(models.Bill)
        .filter(models.Bill.carrier_id == carrier_id)
        .filter(models.Bill.billed_date == billed_date)
        .filter(models.Bill.bill_due_date == due_date)
        .first()
    )


# Products
def get_product(db: Session, product_name: str):
    return (
        db.query(models.Product)
        .filter(models.Product.product_name == product_name)
        .first()
    )


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductBase):
    db_product = models.Product(
        product_name=product.product_name,
        product_description=product.product_description,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_details(db: Session, product_name: str, product_description: str):
    return (
        db.query(models.Product)
        .filter(models.Product.product_name == product_name)
        .filter(models.Product.product_description == product_description)
        .first()
    )


# Carriers
def get_carrier(db: Session, carrier_name: str):
    return (
        db.query(models.Carrier)
        .filter(models.Carrier.carrier_name == carrier_name)
        .first()
    )


def get_carrier(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Carrier).offset(skip).limit(limit).all()


def create_carrier(db: Session, carrier: schemas.CarriersBase):
    db_carrier = models.Carrier(
        carrier_name=carrier.carrier_name,
        account_number=carrier.account_number,
    )
    db.add(db_carrier)
    db.commit()
    db.refresh(db_carrier)
    return db_carrier


def get_carrier_by_details(db: Session, carrier_name: str, account_number: str):
    return (
        db.query(models.Carrier)
        .filter(models.Carrier.carrier_name == carrier_name)
        .filter(models.Carrier.account_number == account_number)
        .first()
    )
