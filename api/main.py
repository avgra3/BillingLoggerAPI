from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from .
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Product
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_details(
        db,
        product_name=product.product_name,
        product_description=product.product_description,
    )
    if db_product:
        raise HTTPException(status_code=400, detail="product already exists!")
    return crud.create_product(db=db, product=product)


# Get All Products
@app.get("/products/", response_model=list[schemas.Product])
def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


# Create Carrier
@app.post("/carriers/", response_model=schemas.Carriers)
def create_carrier(carrier: schemas.CarriersBase, db: Session = Depends(get_db)):
    db_product = crud.get_carrier_by_details(
        db,
        carrier_name=carrier.carrier_name,
        account_number=carrier.account_number,
    )
    if db_product:
        raise HTTPException(status_code=400, detail="carrier already exists!")
    return crud.create_carrier(db=db, carrier=carrier)


# Get All Carriers
@app.get("/carriers/", response_model=list[schemas.Carriers])
def read_carrier(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carriers = crud.get_carrier(db, skip=skip, limit=limit)
    return carriers


# Create a Bill
@app.post("/bills/", response_model=schemas.Bills)
def create_bill(bill: schemas.BillsBase, db: Session = Depends(get_db)):
    db_bill = crud.get_bill_by_details(
        db,
        carrier_id=bill.carrier_id,
        billed_date=bill.billed_date,
        due_date=bill.bill_due_date,
    )
    if db_bill:
        raise HTTPException(status_code=400, detail="bill already exists!")
    return crud.create_bill(db=db, bill=bill)


# Get All Bills
@app.get("/bills/", response_model=list[schemas.Bills])
def read_bill(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bills = crud.get_bills(db, skip=skip, limit=limit)
    return bills
