import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(250), unique=True)
    password = Column(String(250))

    favorites = relationship("Favorite")
   
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

    favorites = relationship("Favorite")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))

    favorites = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    user = relationship("User")
    character = relationship("Character")
    planet = relationship("Planet")

    # Relationships
    user = relationship("User")
    character = relationship("Character")
    planet = relationship("Planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
