from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float

import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()
class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key = True)
    name = Column(String(225))
    color = Column(String(255))
    age = Column(Integer)
    
myDog = Dog(name="rocco",color="brown",age=3)

engine = create_engine('sqlite:///pets.sqlite')
conn = engine.connect()

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

session.add(myDog)
session.commit()
myDogToo = Dog(name="pepe",color="blue",age=10)
session.add(myDogToo)
session.commit()

dog_list = session.query(Dog)
for aDog in dog_list:
    print('my dog is:', aDog.name,'and is', aDog.color )
