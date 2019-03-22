from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class BaseballPlayer(Base):
  __tablename__ = "player"
  player_id = Column(String, primary_key=True)
  birth_year = Column(Integer)
  birth_month = Column(Integer)
  birth_day = Column(Integer)
  birth_country = Column(String)
  birth_state = Column(String)
  birth_city = Column(String)
  name_first = Column(String)
  name_last = Column(String)
  name_given = Column(String)
  weight = Column(Integer)
  height = Column(Integer)
  bats = Column(String)
  throws = Column(String)
  debut = Column(String)
  final_game = Column(String)

# Create Database Connection
engine = create_engine('sqlite:///../Resources/database.sqlite')
Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# Print all of the player names in the database
players = session.query(BaseballPlayer)
for player in players:
  print(player.name_given)

# Find the number of players from the USA
usa = session.query(BaseballPlayer).    filter(BaseballPlayer.birth_country == 'USA').count()
print("There are {} players from the USA".format(usa))

# Find those players who were born before 1990
born_before_1990 = session.query(BaseballPlayer).    filter(BaseballPlayer.birth_year < 1990).count()
    
print("{} players were born before 1990".format(born_before_1990))

# Find those players from the USA who were born after 1989
born_after_1989 = session.query(BaseballPlayer).    filter(BaseballPlayer.birth_year > 1989).filter(BaseballPlayer.birth_country == "USA").    count()
print("{} USA players were born after 1989".format(born_after_1989))

