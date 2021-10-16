from pymongo import MongoClient
from pprint import pprint
from settings import mongo_uri

uri = mongo_uri()
print(uri)
