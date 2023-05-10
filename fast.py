# 1. Library imports
import uvicorn
from fastapi import FastAPI
import mysql.connector

from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class Fly(BaseModel):
    FL_DATE: str
    AIRLINE_ID: int
    ORIGIN_AIRPORT_ID: int
    DEST_AIRPORT_ID: int
    DEP_TIME: str
    id: int

class FlyRepository:
    @staticmethod
    async def find_all():
        connection = mysql.connector.connect(
            host="myservernamekamel.mysql.database.azure.com",
            user="kamel",
            password="1234@Simplon",
            database="airlines"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM janvier LIMIT 5")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [Fly(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    @staticmethod
    async def search(term):
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dog WHERE CONCAT(name, breed) LIKE %s", ('%' + term + '%',))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [Fly(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    @staticmethod
    async def add(fly):
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO test (FL_DATE, AIRLINE_ID, ORIGIN_AIRPORT_ID, DEST_AIRPORT_ID, DEP_TIME) VALUES (%s, %s, %s, %s, %s)", (fly.FL_DATE, fly.AIRLINE_ID, fly.ORIGIN_AIRPORT_ID, fly.DEST_AIRPORT_ID, fly.DEP_TIME))
        connection.commit()
        fly.id = cursor.lastrowid
        cursor.close()
        connection.close()

@app.get("/flys")
async def get_flys():
    flys = await FlyRepository.find_all()
    return flys

@app.get("/search")
async def search_flys(term: str):
    flys = await FlyRepository.search(term)
    return flys

@app.post("/flys")
async def add_fly(fly: Fly):
    await FlyRepository.add(fly)
    return {"message": "Fly added successfully"}


# cnx = mysql.connector.connect(user="kamel", password="1234@Simplon", host="myservernamekamel.mysql.database.azure.com", port=3306, database="airlines")

# # 2. Create the app object
# app = FastAPI()

# # 3. Index route, opens automatically on http://127.0.0.1:8000
# @app.get('/')
# def index():

#     return {'message': 'Hello, stranger'}

# # 4. Route with a single parameter, returns the parameter within a message
# #    Located at: http://127.0.0.1:8000/AnyNameHere
# @app.get('/{name}')
# def get_name(name: str):
#     sql_query = "SELECT TOP 5 * FROM {table}"

#     return {'message': f'Hello, {name}'}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
