# Import SQL Alchemy
from sqlalchemy import create_engine

# Import PyMySQL (Not needed if mysqlclient is installed)
import pymysql
pymysql.install_as_MySQLdb()

# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float

# Create Surfer and Board classes
# ----------------------------------
class Surfer(Base):
    __tablename__ = 'surfers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hometown = Column(String(255))
    wipeouts = Column(Integer)
    rank = Column(Integer)

class Board(Base):
    __tablename__ = 'surfboards'
    id = Column(Integer, primary_key=True)
    surfer_id = Column(Integer)
    board_name = Column(String(255))
    color = Column(String(255))
    length = Column(Integer)
    
# Create specific instances of the Surfer and Board classes
surferjoe = Surfer(name="Joe-Seppi",hometown="Zephyr Shores, CA", wipeouts=42,rank=2)
joeboard = Board(surfer_id=1,board_name="Diametrius Long",color="Platinum",length=72)
# ----------------------------------
# Create a new surfer named "Bruno"
surferbruno = Surfer(name="Bruno",hometown="Songbird Waves, HI", wipeouts=94,rank=5)
# Create a new board and associate it with a surfer's ID
brunoboard = Board(surfer_id=2,board_name="Baphomets Sling",color="Yellow-Green",length=66)   

# Create Database Connection
import pymysql
pymysql.install_as_MySQLdb()
engine = create_engine('sqlite:///pets.sqlite')
conn = engine.connect()
# ----------------------------------
# Establish Connection to MySQL
engine = create_engine('sqlite:///pets.sqlite')
conn = engine.connect()

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# Create both the Surfer and Board tables within the database
session.add(surferjoe)
session.add(surferbruno)
session.add(joeboard)
session.add(brunoboard)
session.commit()

my_list = session.query(Surfer)
my_list[1].hometown
