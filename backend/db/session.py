from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

POSTGRES_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
