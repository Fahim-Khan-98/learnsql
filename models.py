
from sqlalchemy import Column, MetaData, Table, String, Integer, create_engine
from sqlalchemy.orm import declarative_base

dburl = "sqlite:///database.db"

engine = create_engine(dburl)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key=True)
    name = Column(String)
    age = Column (Integer)


Base.metadata.create_all(engine)