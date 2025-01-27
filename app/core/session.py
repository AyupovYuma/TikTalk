from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db(): #подключение к бд
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models.user import User
    Base.metadata.create_all(bind=engine)