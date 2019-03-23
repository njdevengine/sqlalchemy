# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///../Resources/dow.sqlite", echo=False)

inspector = inspect(engine)
inspector.get_table_names()

# Get a list of column names and types
columns = inspector.get_columns('dow')
for c in columns:
    print(c['name'], c["type"])
# columns

engine.execute('SELECT * FROM dow LIMIT 5').fetchall()

# Reflect Database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)
Dow = Base.classes.dow

session = Session(engine)

# Total dates
session.query(func.count(Dow.date)).all()

# Earliest Date
session.query(Dow.date).order_by(Dow.date).first()

# Latest Date
session.query(Dow.date).order_by(Dow.date.desc()).first()

#greater than march 1, 2011
session.query(Dow.date).\
    filter(Dow.date > '2011-03-01').\
    order_by(Dow.date).all()
    
#https://docs.sqlalchemy.org/en/latest/dialects/sqlite.html

import datetime as dt

# Print a date object and a datetime object 
print(dt.date.today())
print(dt.date(2017, 1 ,31))

print(dt.datetime.utcnow())
print(dt.datetime(2017, 1, 31))

# date 1 week ago from today
week_ago = dt.date.today() - dt.timedelta(days=7)

# Query for the Dow closing price for `CSCO` 1 week before `2011-04-08` using the datetime library
query_date = dt.date(2011, 4, 8) - dt.timedelta(days=7)
print("Query Date: ", query_date)

session.query(Dow.date, Dow.close_price).\
    filter(Dow.stock == 'CSCO').\
    filter(Dow.date == query_date).all()
    
# Parse out just the day from the datetime object
dt.date.today().strftime("%d")

# Query for all dates matching the 
# following date string in the format `%d`
date_str = "14"
session.query(Dow.date).\
    filter(func.strftime("%d", Dow.date) == date_str).all()
