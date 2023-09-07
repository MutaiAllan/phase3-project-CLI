from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.movie import Movie
from models.director import Director
from models.base import Base
from models.genre import Genre

DATABASE_URL ="sqlite:///movielist.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

director1 = Director("Allan")
director2 = Director("Mutai")
genre1 = Genre("Fiction")
genre2 = Genre("Crime")
movie1 = Movie("Mr.Robot", director1, genre1)
movie2 = Movie("Wisdom of crowd", director2, genre2)


session.add(director1)
session.add(director2)
session.add(movie1)
session.add(movie2)

session.commit()

all_directors = session.query(Director).all()
for director in all_directors:
    print("Director name: ", director.name)
    for movie in director.movies:
        print("Movie: ", movie.title)

    





