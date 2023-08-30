from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database path
SQLALCHEMY_DATABASE_URL = "sqlite:///./billing.db"

# Create engine to connect to sqlite database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# For each instance of a session, implement a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inherit the below to create each database model and classes
Base = declarative_base()
