from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import create_session, sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from flask import g


load_dotenv()

# Connects to database using the import env variable
engine = create_engine(getenv("DB_URL"), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)

def get_db():
    if "db" not in g: 
        #this stores Database connetion within the app context
        g.db = Session()
    return g.db

    