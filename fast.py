

# 1. Library imports
import uvicorn
from model import IrisModel, IrisSpecies
# from pydantic import BaseModel
# import mysql.connector
# from fastapi import FastAPI
# import databases
# import sqlalchemy
# import pymysql
# import pymysql.cursors
from fastapi import FastAPI
import pymysql

app = FastAPI()



# Configurer la connexion à la base de données MySQL
conn = pymysql.connect(
     host="myservernamekamel.mysql.database.azure.com",
            user="kamel",
            password="1234@Simplon",
            database="airlines",
)

# Définir les routes de l'API
@app.get("/")
async def get_items():
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()
    # Retourner les résultats de l'API
    return {"items": results}

@app.get("/janvier")
async def get_items():
    # Effectuer des opérations sur la base de données
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM janvier LIMIT 5")
        results = cursor.fetchall()
    # Retourner les résultats de l'API
    return {"items": results}
# # 4. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    # uvicorn.run('fast:app', host='0.0.0.0', port=8000)
# app = FastAPI()
# # Configurer la connexion à la base de données
# DATABASE_URL = "mysql+pymysql://kamel:1234@Simplon@myservernamekamel.mysql.database.azure.com:3306/airlines"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# # Définir une table de modèle simple
# items = sqlalchemy.Table(
#     "items",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(50)),
# )

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(bind=engine)

# # Routes de l'API
# @app.get("/items")
# async def get_items():
#     query = items.select()
#     results = await database.fetch_all(query)
#     return {"items": results}

# @app.post("/items")
# async def create_item(name: str):
#     query = items.insert().values(name=name)
#     await database.execute(query)
#     return {"message": "Item created"}

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# # 2. Create app and model objects
# app = FastAPI()
# model = IrisModel()


# @app.get('/co')
# def db_connection():

#     conn = None

#     try:
#         conn = mysql.connector.connect(
#             host="myservernamekamel.mysql.database.azure.com",
#             user="kamel",
#             password="1234@Simplon",
#             database="airlines"
#         )
#         return {'message': f'La bdd est co youpi'}
#     except mysql.connector.Error as error:
#         return {'message': f'erreor bro {error}'}
#     finally:
#         if conn is not None:
#             return {'message': f'la co est vide ????'}



# # 3. Expose the prediction functionality, make a prediction from the passed
# #    JSON data and return the predicted flower species with the confidence
# @app.get('/predict')
# def predict_species(iris: IrisSpecies):
#     data = iris.dict()
#     prediction, probability = model.predict_species(
#         data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
#     )
#     return {
#         'prediction': prediction,
#         'probability': probability
#     }




# app = FastAPI()
# # Configurer la connexion à la base de données
# DATABASE_URL = "mysql+pymysql://kamel:1234@Simplon@myservernamekamel.mysql.database.azure.com:3306/airlines"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# # Définir une table de modèle simple
# items = sqlalchemy.Table(
#     "items",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(50)),
# )

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(bind=engine)

# # Routes de l'API
# @app.get("/items")
# async def get_items():
#     query = items.select()
#     results = await database.fetch_all(query)
#     return {"items": results}

# @app.post("/items")
# async def create_item(name: str):
#     query = items.insert().values(name=name)
#     await database.execute(query)
#     return {"message": "Item created"}

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# # 2. Create app and model objects
# app = FastAPI()
# model = IrisModel()


# @app.get('/co')
# def db_connection():

#     conn = None

#     try:
#         conn = mysql.connector.connect(
#             host="myservernamekamel.mysql.database.azure.com",
#             user="kamel",
#             password="1234@Simplon",
#             database="airlines"
#         )
#         return {'message': f'La bdd est co youpi'}
#     except mysql.connector.Error as error:
#         return {'message': f'erreor bro {error}'}
#     finally:
#         if conn is not None:
#             return {'message': f'la co est vide ????'}



# # 3. Expose the prediction functionality, make a prediction from the passed
# #    JSON data and return the predicted flower species with the confidence
# @app.get('/predict')
# def predict_species(iris: IrisSpecies):
#     data = iris.dict()
#     prediction, probability = model.predict_species(
#         data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
#     )
#     return {
#         'prediction': prediction,
#         'probability': probability
#     }





# # 1. Library imports
# import uvicorn
# from fastapi import FastAPI
# from pydantic import BaseModel
# import mysql.connector
# # Imports
# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from routers.user import view as userview
# # from database import engine
# # from connection_pool import database_instance
# # from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()


# def db_connection():

#     conn = None

#     try:
#         conn = mysql.connector.connect(
#             host="myservernamekamel.mysql.database.azure.com",
#             user="kamel",
#             password="1234@Simplon",
#             database="airlines"
#         )
#         print("la bdd est connecté")
#     except mysql.connector.Error as error:
#         print(error)
#     finally:
#         if conn is not None:
#             return conn



# @app.get("/")
# async def root():
#     return {"message": "Bienvenue dans l'API de prédiction de la résistance à la compression du béton"}

# class Fly(BaseModel):
#     FL_DATE: str
#     AIRLINE_ID: int
#     ORIGIN_AIRPORT_ID: int
#     DEST_AIRPORT_ID: int
#     DEP_TIME: str
#     id: int

# class FlyRepository:
#     @staticmethod
#     async def find_all():
#         connection = mysql.connector.connect(
#             host="myservernamekamel.mysql.database.azure.com",
#             user="kamel",
#             password="1234@Simplon",
#             database="airlines"
#         )
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM janvier LIMIT 5")
#         rows = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return [Fly(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    # @staticmethod
    # async def add(fly):
    #     connection = mysql.connector.connect(
    #         host="localhost",
    #         user="your_username",
    #         password="your_password",
    #         database="your_database"
    #     )
    #     cursor = connection.cursor()
    #     cursor.execute("INSERT INTO test (FL_DATE, AIRLINE_ID, ORIGIN_AIRPORT_ID, DEST_AIRPORT_ID, DEP_TIME) VALUES (%s, %s, %s, %s, %s)", (fly.FL_DATE, fly.AIRLINE_ID, fly.ORIGIN_AIRPORT_ID, fly.DEST_AIRPORT_ID, fly.DEP_TIME))
    #     connection.commit()
    #     fly.id = cursor.lastrowid
    #     cursor.close()
    #     connection.close()

# @app.get("/flys")

# async def get_flys():
#     flys = await FlyRepository.find_all()
#     return flys

# @app.get("/search")
# async def search_flys(term: str):
#     flys = await FlyRepository.search(term)
#     return flys

# @app.post("/flys")
# async def add_fly(fly: Fly):
#     await FlyRepository.add(fly)
#     return {"message": "Fly added successfully"}


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
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
