from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from .base import Base
from .associations import director_movie_association

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    directors = relationship("Director", secondary=director_movie_association, back_populates="movies")

    def __init__(self, title):
        self.title = title

    def add_director(self, director):
        self.directors.append(director)
