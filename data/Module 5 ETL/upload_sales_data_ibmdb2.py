import pandas as pd


# This program requires the python module ibm-db to be installed.
# Install it using the below command
# python3 -m pip install ibm-db

import ibm_db

# connectction details

dsn_hostname = "2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "gtp43120"        # e.g. "abc12345"
dsn_pwd = "gFXKiQEtpIMBjRPv"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "30756"                # e.g. "50000" 
dsn_database = "bludb"            # i.e. "BLUDB"
dsn_driver = "{IBM DB2 ODBC DRIVER}" # i.e. "{IBM DB2 ODBC DRIVER}"           
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              # i.e. "SSL"

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

# create connection
conn = ibm_db.connect(dsn, "", "")
print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)


df = pd.read_csv("sales-csv3mo8i5SHvta76u7DzUfhiw.csv")



# print(df.head(5))

# create table
SQL = """CREATE TABLE IF NOT EXISTS sales_data(rowid INTEGER PRIMARY KEY NOT NULL,product_id varchar(255) NOT NULL,customer_id varchar(255) NOT NULL,price INT,quantity INT,timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

create_table = ibm_db.exec_immediate(conn, SQL)

print("Table created")

# insert data

SQL = "INSERT INTO sales_data(rowid,product_id,customer_id,price,quantity, timestamp)  VALUES(?,?,?,?,?,?);"
stmt = ibm_db.prepare(conn, SQL)
for index, row in df.iterrows():
    ibm_db.execute(stmt, tuple(row.values))

SQL="SELECT * FROM sales_data"
stmt = ibm_db.exec_immediate(conn, SQL)
tuple = ibm_db.fetch_tuple(stmt)
while tuple != False:
    print (tuple)
    tuple = ibm_db.fetch_tuple(stmt)
# export the fields name and type from collection test into the file data.csv



# close connection
ibm_db.close(conn)