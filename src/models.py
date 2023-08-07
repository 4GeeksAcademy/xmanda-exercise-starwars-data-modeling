import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20))
    diameter = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    orbital_period = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20))
    birth_year = Column(String(20))
    height = Column(Integer)
    eye_color = Column(String(20))
    skin_color = Column(String(20))
    world = Column(String(20), ForeignKey('planets.ID'), unique=True)
    planets = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20)) 
    model = Column(String(20))
    manufacturer = Column(String(20))
    vehicle_class = Column(String(20))
    crew = Column(Integer)
    pilots = Column(String(20), ForeignKey('characters.ID'), unique=True)
    characters = relationship(Characters)

class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    ID = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.ID'))
    characters = relationship(Characters)

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    ID = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.ID'))
    planets = relationship(Planets)

class Favorite_Vehicle(Base):
    __tablename__ = 'favorite_vehicle'
    ID = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.ID'))
    vehicles = relationship(Vehicles)

class Favorites(Base):
    __tablename__ = "favorites"
    ID = Column(Integer, primary_key=True)
    favorite_character_id = Column(Integer, ForeignKey("favorite_character.ID"), unique=True)
    favorite_character = relationship(Favorite_Character)
    favorite_planet_id = Column(Integer, ForeignKey("favorite_planet.ID"), unique=True)
    favorite_planet = relationship(Favorite_Planet)
    favorite_vehicle_id = Column(Integer, ForeignKey("favorite_vehicle.ID"), unique=True)
    favorite_vehicle = relationship(Favorite_Vehicle)


class User(Base):
    __tablename__ = "user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20) unique=True)
    email = Column(String(30), unique=True)
    favorites_ID = Column(Integer, ForeignKey("favorites.ID"), unique=True)
    favorites = relationship(Favorites)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
