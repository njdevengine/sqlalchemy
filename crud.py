from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Define our pet table
class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    age = Column(Integer)
    
# Right now, this table only exists in python and not in the actual database
Base.metadata.tables

# Create our database engine
engine = create_engine('sqlite:///pets.sqlite')

# This is where we create our tables in the database
Base.metadata.create_all(engine)

# The ORM’s “handle” to the database is the Session.
from sqlalchemy.orm import Session
session = Session(engine)

######CREATE######

# Note that adding to the session does not update the table. It queues up those queries.
session.add(Pet(name='Justin Timbersnake', type='snek', age=2))
session.add(Pet(name='Pawtrick Stewart', type='good boy', age=10))
session.add(Pet(name='Godzilla', type='iguana', age=1))
session.add(Pet(name='Marshmallow', type='polar bear', age=4))

# The data hasn't been added yet
engine.execute('select * from pet').fetchall()

# We can use the new attribute to see the queue of data ready to go into the database
session.new

# commit() flushes whatever remaining changes remain to the database, and commits the transaction.
session.commit()

# Nothing new to add
session.new

# query the database
session.query(Pet.name, Pet.type, Pet.age).all()

######UPDATE######

# Create a query and then run update on it
pet = session.query(Pet).filter_by(name="Marshmallow").first()
pet.age += 1

# For modifications, we can use the dirty attribute
session.dirty

# Commit Transaction
session.commit()

# Session is up-to-date
session.dirty

session.query(Pet.id, Pet.name, Pet.type, Pet.age).all()

######DELETE#####
# Create a query and then delete the row collected
pet = session.query(Pet).filter_by(id=4).delete()
session.commit()

session.query(Pet.id, Pet.name, Pet.type, Pet.age).all()
