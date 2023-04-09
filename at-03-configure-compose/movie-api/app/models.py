from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)
    genre = Column(String)
    year = Column(Integer)

