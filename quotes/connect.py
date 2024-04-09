import os
from urllib.parse import quote_plus
from pymongo import MongoClient
import psycopg2
from dotenv import load_dotenv

load_dotenv()

user = os.environ.get('MG_USER')
password = os.environ.get('MG_PASSWORD')

escaped_user = quote_plus(user)
escaped_password = quote_plus(password)

def get_mongodb():
    client = MongoClient(f'mongodb+srv://{escaped_user}:{escaped_password}@cluster0.j1fuex0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client.hw
    return db