from sqlalchemy import create_engine, Column, Integer, String

from src.config.database import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)
    genre = Column(String)
