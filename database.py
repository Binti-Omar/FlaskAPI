# SQLAlchemy is an ORM.Object relational mapping.
# Helps execute queries using methods.
# Define the table structure is classes/models.

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String,DateTime
# from datetime import datetime

class Base(DeclarativeBase):
    pass

# Map Users table to user class
class Employee(Base):
    __tablename__="employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location : Mapped[str] = mapped_column(String(100))
    age : Mapped[int] = mapped_column()
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class Authentication(Base):
    __tablename__ = "user_authentication"  
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100),unique=True)
    hashed_pw: Mapped[str] = mapped_column(String(300))
    created_at: Mapped[DateTime] = mapped_column(DateTime)