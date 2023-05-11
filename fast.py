# 1. Library imports
import uvicorn
from typing import List
from models import Test
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import pymysql
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = FastAPI()

# Récupérer l'URL de la base de données à partir des variables d'environnement
database_url = os.getenv("DATABASE_URL")

# Extraire les composants de l'URL de la base de données
url_components = urlparse(database_url)
db_host = url_components.hostname
db_user = url_components.username
db_password = url_components.password
db_name = url_components.path.strip("/")

# Configurer la connexion à la base de données MySQL
conn = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
def fetch_items(table_name: str, limit: int = None) -> List[Test]:
    # Perform operations on the database
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table_name}"
        if limit is not None:
            query += f" LIMIT {limit}"
        cursor.execute(query)
        results = cursor.fetchall()

    # Convert the results to a list of Test objects
    items = [Test(**row) for row in results]
    return items


@app.get("/items/{table_name}")
async def get_items(table_name: str, limit: int = None) -> List[Test]:
    if table_name not in ["test", "janvier"]:
        raise HTTPException(status_code=404, detail="Table not found")

    items = fetch_items(table_name, limit)
    return items

# Définir les routes de l'API
@app.get("/")
async def get_items() -> List[Test]:
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()

    # Convertir les résultats en une liste d'objets Test
    items = []
    for row in results:
        test_dict = {
            "id": row[0],
            "FL_DATE": row[1],
            "AIRLINE_ID": row[2],
            "ORIGIN_AIRPORT_ID": row[3],
            "DEST_AIRPORT_ID": row[4],
            "DEP_TIME": row[5]
        }
        test = Test(**test_dict)
        items.append(test)

    # Retourner les résultats de l'API
    return items

@app.get("/janvier")
async def get_items():
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM janvier LIMIT 5")
        results = cursor.fetchall()
    # Retourner les résultats de l'API
    return {"items": results}


@app.post("/add")
async def create_item(item: Test):
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        query = "INSERT INTO test (FL_DATE, AIRLINE_ID, ORIGIN_AIRPORT_ID, DEST_AIRPORT_ID, DEP_TIME) " \
                "VALUES (%s, %s, %s, %s, %s)"
        values = (item.FL_DATE, item.AIRLINE_ID, item.ORIGIN_AIRPORT_ID, item.DEST_AIRPORT_ID, item.DEP_TIME)
        cursor.execute(query, values)
        conn.commit()

    return {"message": "Item created successfully"}

    #         # Récupérer l'ID de la nouvelle instance
    #     new_item_id = cursor.lastrowid

    #     # Exécuter une requête SELECT pour récupérer la nouvelle instance
    #     query = "SELECT * FROM test WHERE id = %s"
    #     cursor.execute(query, new_item_id)
    #     new_item_data = cursor.fetchone()

    # # Créer une nouvelle instance de Test à partir des données récupérées
    # new_item = Test(*new_item_data)

    # return new_item


# # 4. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
