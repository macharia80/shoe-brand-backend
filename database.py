# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use SQLite database stored in a local file called 'shoe.db'
DATABASE_URL = "sqlite:///./shoe.db"

# For SQLite, check_same_thread=False is needed in most cases
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to declare models
Base = declarative_base()