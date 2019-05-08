#https://docs.sqlalchemy.org/en/latest/core/engines.html
# SQL Alchemy
import urllib
import sqlalchemy as sa
from sqlalchemy import create_engine

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=servername01;"
                                 "DATABASE=DATABASENAME;"
                                 "Trusted_Connection=yes")
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

# Query All Records in the the Database
# data = engine.execute("""SELECT * FROM TABLENAME;""")
# for record in data:
#     print(record)
    
import pandas as pd
con = engine.connect()
data = pd.read_sql("SELECT * FROM TABLENAME;",con)
data.head()
