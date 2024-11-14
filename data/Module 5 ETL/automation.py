# Import libraries required for connecting to mysql

import mysql.connector

# connect to database
# You can get the Hostname and Password from the connection information section of Mysql 
connection = mysql.connector.connect(user='root', password='b2wowFcIsrW6J8BhmgKg9LDj',host='172.21.116.31',database='Sales')

# create cursor

cursor_mysql = connection.cursor()

# Import libraries required for connecting to DB2 or PostgreSql

import psycopg2

# connectction details

dsn_hostname = '172.21.96.114'
dsn_user='postgres'        # e.g. "abc12345"
dsn_pwd ='w8h8hCKBKE80lk21vneqAzAN'      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port ="5432"                # e.g. "50000" 
dsn_database ="Sales"           # i.e. "BLUDB"

# create connection

conn = psycopg2.connect(
database=dsn_database, 
user=dsn_user,
password=dsn_pwd,
host=dsn_hostname, 
port= dsn_port
)

#Crreate a cursor onject using cursor() method

cursor = conn.cursor()

# Connect to MySQL

# Connect to DB2 or PostgreSql

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    SQL = """SELECT ROWID FROM  SALES_DATA ORDER BY ROWID DESC LIMIT 1"""
    cursor.execute(SQL)
    rows = cursor.fetchall()
    # conn.commit()
    # conn.close()
    for row in rows:
        # print(row)
        return  row[0]

last_row_id = get_last_rowid()

print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    records = []
    SQL = f"SELECT * FROM sales_data WHERE ROWID > {rowid}" 
    cursor_mysql.execute(SQL)
    for row in cursor_mysql.fetchall():
        records.append(row)
    return records
    
new_records = get_latest_records(last_row_id)


print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.




def insert_records(records):
    for record in records:
        SQL="INSERT INTO  public.sales_data(rowid,product_id,customer_id,quantity) values(%s,%s,%s,%s) ON CONFLICT (rowid) DO NOTHING;" 
        cursor.execute(SQL,record);
        conn.commit()
        
insert_records(new_records)

print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()
# disconnect from DB2 or PostgreSql data warehouse 
conn.close()
# End of program
