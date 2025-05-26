from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(getenv("MONGO_URI"))
db = client["image_moderation"]
tokens = db["tokens"]
usages = db["usages"]
