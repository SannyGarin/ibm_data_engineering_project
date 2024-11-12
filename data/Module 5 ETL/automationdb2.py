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


def get_last_rowid():

    SQL = """SELECT ROWID FROM  SALES_DATA ORDER BY ROWID DESC LIMIT 1"""
    select_last_rowid = ibm_db.exec_immediate(conn, SQL)
    tuple = ibm_db.fetch_tuple(select_last_rowid)
    return tuple[0]


print(get_last_rowid())

last_row = int(get_last_rowid())

import mysql.connector
# connect to database
# You can get the Hostname and Password from the connection information section of Mysql 
connection = mysql.connector.connect(user='root', password='uh6tqyfE07NuIm4PhCgV3lR1',host='172.21.26.137',database='Sales')
# create cursor
cursor = connection.cursor()

def get_latest_records():

    SQL = f"SELECT * FROM sales_data WHERE ROWID > {last_row}"
    cursor.execute(SQL)
    return cursor.fetchall()
print(get_latest_records())


def insert_records(): 
    SQL = "INSERT INTO products(rowid,product,category)  VALUES(?,?,?);"
    stmt = ibm_db.prepare(conn, SQL)
    for row in get_latest_records():


# insert data

SQL = "INSERT INTO products(rowid,product,category)  VALUES(?,?,?);"
stmt = ibm_db.prepare(conn, SQL)
row1 = (1,'Television','Electronics')
ibm_db.execute(stmt, row1)

row2 = (2,'Laptop','Electronics')
ibm_db.execute(stmt, row2)

row3 = (3,'Mobile','Electronics')
ibm_db.execute(stmt, row3)

# close connection
connection.close()


