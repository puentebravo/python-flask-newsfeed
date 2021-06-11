from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import create_session, sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm.session import Session

load_dotenv()

# Connects to database using the import env variable
engine = create_engine(getenv("DB_URL"), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()