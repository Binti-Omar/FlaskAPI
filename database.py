# SQLAlchemy is an ORM.Object relational mapping.
# Helps execute queries using methods.
# Define the table structure is classes/models.

from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

# Map Users table to user class
class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location : Mapped[str] = mapped_column(String(100))
    