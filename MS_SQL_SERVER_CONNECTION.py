import urllib
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd

#DO ONE CONNECTION & QUERY####################################################
#THIS IS MICROSOFT AUTHENTICATION
# params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
#                                  "SERVER=server_name;"
#                                  "DATABASE=DB_NAME;"
#                                  "Trusted_Connection=yes")
# engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
# con = engine.connect()
# data = pd.read_sql("SELECT * FROM TABLE_NAME;",con)
# data.head()

#GET THE TABLES OF A DATABASE####################################################
get_tables =r"""
SELECT NAME AS ObjectName
    ,schema_name(o.schema_id) AS SchemaName
    ,type
    ,o.type_desc
FROM sys.objects o
WHERE o.is_ms_shipped = 0
ORDER BY o.NAME;
"""
# pd.read_sql(get_tables,con)

dbs = ['list','of','databases']
tables = ['table1','table2']

#GET TABLES AND SAVE DATA AS CSV
files = []
for i in dbs:
    for n in tables:
        files.append(i+"_"+n+".csv")
        print(i,n,"connected successfully!!")
        params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=server_name;"
                                 "DATABASE="+i+";"
                                 "Trusted_Connection=yes")
        engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        con = engine.connect()
        data = pd.read_sql("SELECT * FROM "+n+";",con)
        data.to_csv('server_tables//'+i+"_"+n+".csv")
        
#READ THE DATA CSVs INTO DATAFRAMES
length = (len(dbs)*len(tables))
my_data = []
for i in range(0,length):
    file = pd.read_csv(r'H:\server_tables\\'+files[i])
    my_data.append(file)
    
#PRINT BASIC TABLE METADATA GET EACH TABLE BY USING my_data[number]
egg = "                 "
for i in range(len(my_data)):
    print("my_data",i,"is:   ",files[i],egg,"COLUMNS: ",str(len(list(my_data[i]))),"/   ROWS: ",str(len(my_data[i])))
    
#PRINT NUMBER OF UNIQUE IDS
ids = []
for i in my_data:
    ids += (list(i["RecordID"]))
print(len(ids))
unique = list(set(ids))
print(len(unique))

#DO ONE CONNECTION & QUERY####################################################
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=my_server_2;"
                                 "DATABASE=my_db_2;"
                                 "Trusted_Connection=yes")
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
con = engine.connect()
tables = pd.read_sql(get_tables,con)
tables = tables[tables.type_desc == "USER_TABLE"]

#GET AND PRINT TABLE NAMES
print(tables.ObjectName.to_list())
def grab(table):
    x = pd.read_sql("SELECT * FROM "+str(table)+";",con)
    return(x)

#grab("table_name")
