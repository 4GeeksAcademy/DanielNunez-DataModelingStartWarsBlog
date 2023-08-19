import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class User_Favorites(Base):
    __tablename__ = 'People_Favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(200), nullable=False)
    favorite = relationship(User_Favorites)

class People(Base):
    __tablename__ = 'People'
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
    favorite = relationship(User_Favorites)

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(100))
    gravity = Column(String(100))
    favorite = relationship(User_Favorites)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
