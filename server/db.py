from pymongo import MongoClient
from pprint import pprint


client = pymongo.MongoClient("mongodb+srv://dbUser:<password>@cluster0.n2dm7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
