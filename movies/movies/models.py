from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        UniqueConstraint
                        )
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///movie.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Movie(Base):
    '''Model to represent a movie with data from a
    row in the CSV from IMDB.
    '''
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    movie_title = Column('title', String, unique=True)
    actor_name1 = Column('actor1', String)
    actor_name2 = Column('actor2', String)
    actor_name3 = Column('actor3', String)
    director_name = Column('director', String)
    budget = Column('budget', Integer)
    gross = Column('gross', Integer)

    __table_args = (UniqueConstraint('title', 'gross', name='unix_1'))
    
    @classmethod
    def movie_factory(cls, raw_movie_list):
        '''Factory method to build Movie instances.

        Args:
        raw_movie_list - list
        '''
        header = raw_movie_list.pop(0)
        
        movie_title_index = header.index('movie_title')
        actor_name1_index = header.index('actor_1_name')
        actor_name2_index = header.index('actor_2_name')
        actor_name3_index = header.index('actor_3_name')
        director_name_index = header.index('director_name')
        budget_index = header.index('budget')
        gross_index = header.index('gross')
        
        session = Session()
        
        for each in raw_movie_list:
            movie = Movie()
            movie.movie_title = each[movie_title_index]
            movie.actor_name1 = each[actor_name1_index]
            movie.actor_name2 = each[actor_name2_index]
            movie.actor_name3 = each[actor_name3_index]
            movie.director_name = each[director_name_index]
            try:
                movie.budget = int(each[budget_index])
            except ValueError:
                movie.budget = 0
            try:
                movie.gross = int(each[gross_index])
            except ValueError:
                movie.gross = 0
            session.add(movie)

            try:
                session.commit()
                yield movie
            except IntegrityError:
                session.rollback()
                yield None

    def __repr__(self):
        return "<Movie('%s')>" % self.movie_title

    def __str__(self):
        return self.movie_title

Base.metadata.create_all(engine)
