# backend/seed_token.py

from pymongo import MongoClient
from datetime import datetime
import os

# Load env vars from .env if needed (optional)
from dotenv import load_dotenv
load_dotenv()

# Get DB connection string from environment variable or use default
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "image_moderation")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

token_value = "test-secret-token"

# Insert the token
result = db.tokens.insert_one({
    "token": token_value,
    "name": "Test User",
    "created_at": datetime.utcnow()
})

print(f"✅ Seeded token: {token_value} with ID: {result.inserted_id}")
