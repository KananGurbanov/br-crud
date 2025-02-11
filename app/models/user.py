from sqlalchemy import Column, Integer, String, Text
from app.db.db_initializer import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    process_case = Column(String(50), nullable=True)
    text = Column(Text, nullable=True)
    phone_number = Column(String(20), nullable=True)
