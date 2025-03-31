import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(override=True)

POSTGRES_USER = os.environ["DB_USER"]
POSTGRES_PASSWORD = os.environ["DB_PASSWORD"]
POSTGRES_HOST = os.environ.get("DB_HOST_DOCKER", "localhost")
POSTGRES_PORT = os.environ["DB_PORT"]
POSTGRES_DB = os.environ["DB_NAME"]

def get_standard_postgres_connection():
    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def get_database_engine():
    db_url = get_standard_postgres_connection()
    return create_engine(db_url, echo=True)

engine = get_database_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()