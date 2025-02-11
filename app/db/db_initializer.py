from contextlib import contextmanager
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from app.config.config import config  # Import config module
from app.logger.logger import get_logger

#
# Get SQLite configuration values (no port or host needed for SQLite)
DATABASE = config["database"]["name"]  # Example: "test.db" (your SQLite DB file)
DATABASE_URL = f"sqlite:///{DATABASE}"  # SQLite URL format

# MetaData for defining tables
metadata = MetaData()

# Create SQLite engine (no pooling or complex options)
engine = create_engine(DATABASE_URL,
                       echo=False,  # Set to True for logging SQL queries
                       connect_args={"check_same_thread": False})  # Needed for multi-threading support with SQLite

# SessionLocal to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Logger setup
logger = get_logger(__name__)

# Context manager to manage database sessions
@contextmanager
def get_session() -> Session:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()

# FastAPI Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)

