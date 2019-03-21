
#https://docs.sqlalchemy.org/en/latest/core/engines.html

# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:mypass@localhost:3306/sakila')

# Query All Records in the the Database
data = engine.execute("SELECT * FROM sakila.actor")

for record in data:
    print(record)
    
import pandas as pd
con = engine.connect()
data = pd.read_sql("SELECT * FROM sakila.actor",con)
data
