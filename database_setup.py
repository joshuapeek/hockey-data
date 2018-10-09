from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    conference = Column(String(7), nullable=False)
    division = Column(String(12), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'        : self.id,
            'city'      : self.city,
            'name'      : self.name,
            'conference': self.conference,
            'division'  : self.division
        }

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(100))
    position = Column(String(2))
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)
    height = Column(String(10))
    weight = Column(String(8))
    birthdate = Column(String(50))
    birthCity = Column(String(50))
    birthLocation = Column(String(50))
    birthNation = Column(String(50))
    bio = Column(String(2500))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'            : self.id,
            'firstName'     : self.firstName,
            'lastName'      : self.lastName,
            'position'      : self.position,
            'team_id'       : self.team,
            'height'        : self.height,
            'weight'        : self.weight,
            'birthdate'     : self.birthdate,
            'birthCity'     : self.birthCity,
            'birthLocation' : self.birthLocation,
            'birthNation'   : self.birthNation,
            'bio'           : self.bio,
        }

engine = create_engine('sqlite:///hockey.db')
Base.metadata.create_all(engine)
