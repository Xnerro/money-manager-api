from fastapi import APIRouter, Depends, HTTPException, Body, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, func, ForeignKey, Column
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import INTEGER, DATE, VARCHAR, BOOLEAN
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
