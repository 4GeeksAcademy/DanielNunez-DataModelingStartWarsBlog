import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(200), nullable=False)
    favorite = relationship('Favorite', backref='user', lazy=True)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    height = Column(String(100))
    mass = Column(String(100))
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    homeworld = Column(String(100))
    favorite = relationship('Favorite', backref='people', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(100))
    gravity = Column(String(100))
    favorite = relationship('Favorite', backref='planet', lazy=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
