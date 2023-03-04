import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorito = relationship("Favorito")


class Favorito(Base):
    __tablename__= "favorito"
    id = Column(Integer, primary_key=True)
    personajes = Column(String(50),ForeignKey("personaje.name"))
    vehiculos = Column(String(50),ForeignKey("vehiculo.name"))
    Planetas = Column(String(50),ForeignKey("planeta.name"))
    user_email = Column(String(50),ForeignKey("user.email"))
 

class Personaje(Base):
    __tablename__="personaje"
    id = Column(Integer, primary_key=True)
    image = Column(String(100),nullable=False)
    name = Column(String(100), nullable=False)
    species = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    homeworld = Column(String(100), nullable=False)
    height = Column(String(100), nullable=False)
    mass = Column(String(100), nullable=False)
    bornLocation = Column(String(100), nullable=False)
    deadLocation = Column(String(100), nullable=False)
    favorito = relationship("Favorito")

   

class Vehiculo(Base):
    __tablename__="vehiculo"
    id = Column(Integer, primary_key=True)
    image = Column(String(100),nullable=False)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    passengers = Column(String(100), nullable=False)
    cargo_capacity = Column(String(100), nullable=False)
    crew = Column(String(100), nullable=False)
    length = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)
    cost_in_credits = Column(String(100), nullable=False)
    favorito = relationship("Favorito")

class Planeta(Base):
    __tablename__="planeta"
    id = Column(Integer, primary_key=True)
    image = Column(String(100),nullable=False)
    name = Column(String(100), nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    population = Column(String(100), nullable=False)
    diameter = Column(String(100), nullable=False)
    gravity = Column(String(100), nullable=False)
    rotation_period = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)
    favorito = relationship("Favorito")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
