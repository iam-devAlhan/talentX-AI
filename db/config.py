from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.igv4jfg.mongodb.net/?retryWrites=true&w=majority&appName=talentx-cluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database(MONGO_DATABASE)
users_collection = db["users"]
rev_embeddings_collection = db["review_embeddings"]

def connect_db():  
# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(e)
