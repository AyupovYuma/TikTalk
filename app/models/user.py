from sqlalchemy import Column, Integer, String
from app.core.session import Base, engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    loggin = Column(String, unique=True, index=True)
    password_hash = Column(String)