import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = r'C:\Users\SESA647993\Desktop\Continous Learning\Coursera\3. Python Project for Data Engineering\ETL_exercise_Webscraping\top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

html_page = requests.get(url, verify = False).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break 

### LOADING DATA TO A CSV FILE   
df.to_csv(csv_path)
print('Loading data as a csv file completed')
### LOADING DATA TO SQL DATABASE
db_name = 'Movies.db'
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Loading data to SQL database completed')
### QUERYING DATA TO SQL DATABASE
query_statement = 'SELECT * FROM Top_50 LIMIT 5'
df = pd.read_sql(query_statement, conn)
print('Querying data completed')
print(df)
conn.close()