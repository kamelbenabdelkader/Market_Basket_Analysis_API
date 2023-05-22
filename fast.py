# 1. Library imports
import uvicorn
from typing import List
from models import Test,  TableBdd
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

#----------------- Function a placer dans un autre fichier et a refacto-----------------------------#
def fetch_items(table_name: str, limit: int = None) -> List[TableBdd]:
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table_name}"
        if limit is not None:
            query += f" LIMIT {limit}"
        cursor.execute(query)
        results = cursor.fetchall()

    items = []
    for row in results:
        item = TableBdd(
            YEAR=row[0],
            QUARTER=row[1],
            MONTH=row[2],
            DAY_OF_MONTH=row[3],
            DAY_OF_WEEK=row[4],
            FL_DATE=row[5],
            UNIQUE_CARRIER=row[6],
            AIRLINE_ID=row[7],
            CARRIER=row[8],
            TAIL_NUM=row[9],
            FL_NUM=row[10],
            ORIGIN_AIRPORT_ID=row[11],
            ORIGIN_AIRPORT_SEQ_ID=row[12],
            ORIGIN_CITY_MARKET_ID=row[13],
            ORIGIN=row[14],
            ORIGIN_CITY_NAME=row[15],
            ORIGIN_STATE_ABR=row[16],
            ORIGIN_STATE_FIPS=row[17],
            ORIGIN_STATE_NM=row[18],
            ORIGIN_WAC=row[19],
            DEST_AIRPORT_ID=row[20],
            DEST_AIRPORT_SEQ_ID=row[21],
            DEST_CITY_MARKET_ID=row[22],
            DEST=row[23],
            DEST_CITY_NAME=row[24],
            DEST_STATE_ABR=row[25],
            DEST_STATE_FIPS=row[26],
            DEST_STATE_NM=row[27],
            DEST_WAC=row[28],
            CRS_DEP_TIME=row[29],
            DEP_TIME=row[30],
            DEP_DELAY=row[31],
            DEP_DELAY_NEW=row[32],
            DEP_DEL15=row[33],
            DEP_DELAY_GROUP=row[34],
            DEP_TIME_BLK=row[35],
            TAXI_OUT=row[36],
            WHEELS_OFF=row[37],
            WHEELS_ON=row[38],
            TAXI_IN=row[39],
            CRS_ARR_TIME=row[40],
            ARR_TIME=row[41],
            ARR_DELAY=row[42],
            ARR_DELAY_NEW=row[43],
            ARR_DEL15=row[44],
            ARR_DELAY_GROUP=row[45],
            ARR_TIME_BLK=row[46],
            CANCELLED=row[47],
            CANCELLATION_CODE=row[48],
            DIVERTED=row[49],
            CRS_ELAPSED_TIME=row[50],
            ACTUAL_ELAPSED_TIME=row[51],
            AIR_TIME=row[52],
            FLIGHTS=row[53],
            DISTANCE=row[54],
            DISTANCE_GROUP=row[55],
            CARRIER_DELAY=row[56],
            WEATHER_DELAY=row[57],
            NAS_DELAY=row[58],
            SECURITY_DELAY=row[59],
            LATE_AIRCRAFT_DELAY=row[60],
            FIRST_DEP_TIME=row[61],
            TOTAL_ADD_GTIME=row[62],
            LONGEST_ADD_GTIME=row[63],
            Column65=row[64]
        )
        items.append(item)

    # #Pour refacto remplacer par
    # items = []
    # for row in results:
    #     item = TableBdd(*row[:65])
    #     items.append(item)


    # test
    # Retourner les résultats de l'API
    return items




#----------------- Définir les routes de l'API-----------------------------#

#Prendre les mois en vue de faire des KBI ou des graphes
@app.get("/mois/{table_name}")
async def get_items(table_name: str, limit: int = None) -> List[TableBdd]:
    if table_name not in ["janvier","fevrier","mars","avril", "mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]:
        raise HTTPException(status_code=404, detail="Table not found")

    items = fetch_items(table_name, limit=5)
    return items

# Petit test de co avec method get sur le home /
@app.get("/")
async def get_items() -> List[Test]:
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()

    # Convertir les résultats en une liste d'objets Test a refacto par la suite
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

#Ici un exemple detaillé

#apres le app je choisis une method du CRUD
#création (.post), la lecture (.get), la mise à jour (.update) et la suppression (.delete) des données.
# Ici je souhaite simplement recuperer les infos donc j utulise la method .get
#Puis entre paranthése je definis mon point de terminaison .
# Un point de terminaison (ou endpoint en anglais) est une URL spécifique
#à laquelle une application ou un service web peut être accédé.
# Il définit une ressource ou une fonctionnalité particulière fournie par l'API.
# Chaque point de terminaison est associé à une méthode HTTP spécifique
# (comme GET, POST, PUT, DELETE) qui indique l'action à effectuer sur la ressource.
# Bien entendu on peut mettre ce que l'on souhaite comme point de terminaison
# il faut juste etre coherent et que cela soit parlant pour qu'on s'yretrouve

@app.get("/janvier")
async def get_items():
    #le mot-clé "async" est utilisé pour déclarer des fonctions asynchrones
    # qui peuvent contenir des opérations asynchrones,
    # améliorant ainsi les performances de l'API
    # en permettant l'exécution concurrente de plusieurs tâches.
    #La programmation asynchrone permet à une application d'effectuer d'autres tâches
    # pendant l'attente d'une opération asynchrone,
    # plutôt que de bloquer l'exécution jusqu'à ce que l'opération soit terminée.


    # On va ensuite effectuer des opérations sur la base de données
    #nous avons une connexion à la base de données représentée par l'objet conn.
    # La méthode cursor() est appelée sur cette connexion pour obtenir un objet cursor
    # qui nous permet d'exécuter des requêtes sur la base de données.
    with conn.cursor() as cursor:

        #Ensuite, nous utilisons le cursor pour exécuter une requête SQL
        # avec la méthode execute().
        # Dans cet exemple, la requête exécute une instruction SELECT
        # pour récupérer toutes les lignes de la table "janvier"
        # et nous limitons les résultats à 5 en utilisant LIMIT 5.
        cursor.execute("SELECT * FROM janvier LIMIT 5")

        #Une fois que la requête est exécutée,
        # nous utilisons la méthode fetchall() pour récupérer tous les résultats
        # de la requête dans une liste.
        # Ces résultats sont stockés dans la variable results.
        results = cursor.fetchall()

    # Puis on retourne les résultats de l'API
   # Enfin, nous retournons les résultats sous la forme d'un dictionnaire JSON
   # avec la clé "items" qui contient la liste des résultats.
   # Cela signifie que lorsque vous accédez à cet endpoint de l'API,
   # vous recevrez un JSON contenant les cinq premières lignes de la table "janvier".
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




@app.put("/put/{item_id}")
async def update_item(item_id: int, item: Test):
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        query = "UPDATE test SET FL_DATE = %s, AIRLINE_ID = %s, ORIGIN_AIRPORT_ID = %s, DEST_AIRPORT_ID = %s, DEP_TIME = %s " \
                "WHERE id = %s"
        values = (item.FL_DATE, item.AIRLINE_ID, item.ORIGIN_AIRPORT_ID, item.DEST_AIRPORT_ID, item.DEP_TIME, item_id)
        cursor.execute(query, values)
        conn.commit()

    return {"message": f"Item with ID {item_id} updated successfully"}


@app.patch("/patch/{item_id}")
async def update_item(item_id: int, item: Test):
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        query = "UPDATE test SET "
        values = []

        # Générer la clause SET dynamiquement en fonction des valeurs non nulles de l'objet `item`
        if item.FL_DATE is not None:
            query += "FL_DATE = %s, "
            values.append(item.FL_DATE)
        if item.AIRLINE_ID is not None:
            query += "AIRLINE_ID = %s, "
            values.append(item.AIRLINE_ID)
        if item.ORIGIN_AIRPORT_ID is not None:
            query += "ORIGIN_AIRPORT_ID = %s, "
            values.append(item.ORIGIN_AIRPORT_ID)
        if item.DEST_AIRPORT_ID is not None:
            query += "DEST_AIRPORT_ID = %s, "
            values.append(item.DEST_AIRPORT_ID)
        if item.DEP_TIME is not None:
            query += "DEP_TIME = %s, "
            values.append(item.DEP_TIME)

        # Supprimer la virgule finale de la clause SET
        query = query.rstrip(", ")

        # Ajouter la clause WHERE pour mettre à jour l'élément spécifié par item_id
        query += " WHERE id = %s"
        values.append(item_id)

        # Exécuter la requête de mise à jour avec les valeurs fournies
        cursor.execute(query, values)
        conn.commit()

    return {"message": f"Item with ID {item_id} updated successfully"}



@app.delete("/delete/{item_id}")
async def delete_item(item_id: int):
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        query = "DELETE FROM test WHERE id = %s"
        cursor.execute(query, item_id)
        conn.commit()

    return {"message": f"Item with ID {item_id} deleted successfully"}

# # 4. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
