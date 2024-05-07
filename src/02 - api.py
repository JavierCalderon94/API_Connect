from fastapi import FastAPI, HTTPException
import requests
import pandas as pd
import sqlite3
import pickle
import uvicorn
import os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

conn = sqlite3.connect(os.getcwd()+"\\data\\db_investments.db")
cursor = conn.cursor()

model = pickle.load(open(os.getcwd()+'\\data\\advertising_model.pkl','rb'))

app = FastAPI()

# INGEST
@app.post('/ingest')
async def ingest(data: dict):
    if data and 'data' in data:

        for dataingest in data["data"]:
            id = len(list(cursor.execute("SELECT id FROM investments")))
            cursor.execute('''INSERT INTO investments (id, TV, radio, newspaper, sales) 
                VALUES  (?,?,?,?,?)''', (id, dataingest[0], dataingest[1], dataingest[2], dataingest[3]))
            conn.commit()
        return {'message': 'Datos ingresados correctamente'}
    else:
        return "Es necesario algún dato adicional"


#PREDICT
@app.get('/predict')
async def predict(data: dict):
    if data and 'data' in data:

        return { "prediction": model.predict([[data["data"][0][0], data["data"][0][1], data["data"][0][2]]])[0]} 
    else:
        return "Es necesario algún dato adicional"
    
#RETRAIN
@app.post("/retrain")
async def retrain():
    df = pd.read_sql_query("SELECT TV, radio, newspaper, sales FROM investments",conn)
    X = df[["TV", "radio", "newspaper"]]
    y = df["sales"]
    model.fit(X,y)
    return {'message': 'Modelo reentrenado correctamente.'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


