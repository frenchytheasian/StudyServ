import pymongo
from random import randint
from settings import mongo_uri

def get_db():
    uri = mongo_uri()

    client = pymongo.MongoClient(uri)

    db = client.study_spots

    return db

db = get_db()
