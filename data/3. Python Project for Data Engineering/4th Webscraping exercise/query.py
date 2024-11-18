import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup


db_name = 'World_Economies.db'
conn = sqlite3.connect(db_name)
# df.to_sql(table_name, conn, if_exists='replace', index=False)
# # conn.close()

query_statement = "SELECT name FROM sqlite_master WHERE type='table'"
query_statement2 = "SELECT * FROM Countries_by_GDP"
query_statement3 = "SELECT COUNT(*) FROM Countries_by_GDP"
df = pd.read_sql(query_statement3, conn)
print(df)


