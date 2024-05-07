import pandas as pd
import sqlite3
import csv

import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

df = pd.read_csv(os.getcwd()+"\\data\\Advertising.csv", index_col=0)

df.rename(columns={"newpaper":"newspaper"},inplace=True)
df.loc[0,"newspaper"]= 69.2
df["newspaper"] = df["newspaper"].astype(float)

conn = sqlite3.connect(os.getcwd()+'\\data\\db_investments.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE investments (
               id VARCHAR(5),
               TV VARCHAR(64),
               radio VARCHAR(64),
               newspaper VARCHAR(64),
               sales VARCHAR(64))'''
               )

for i in df.index:
    cursor.execute('''INSERT INTO investments (id, TV, radio, newspaper, sales) 
               VALUES  (?,?,?,?,?)''', (list(df.index)[i], df.loc[i,"TV"], df.loc[i,"radio"], df.loc[i,"newspaper"], df.loc[i,"sales"]))
    

conn.commit()
conn.close()
