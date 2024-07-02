from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.meetify

user_collection = database.get_collection("users")
meeting_collection = database.get_collection("meetings")

user_collection.create_index([("email", ASCENDING)], unique=True)
