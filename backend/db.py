import pymongo
from settings import mongo_uri

def get_db():
    uri = mongo_uri()

    client = pymongo.MongoClient(uri)

    db = client['study_spots']

    return db

db = get_db()

def get_study_spots(location):
    cursor = db['spots'].find({'zipcode': 63121})
    spots = list(cursor)
    return spots

def get_study_spot(id):
    return {}

def add_study_spot(name, zipcode, location):
    """
    Creates a new study spot with the following fields:
    """

    spot_doc = {'spot_id': 2, 'name': name, 'zipcode': zipcode, 'location': location, 'attributes': [], 'avg_rating': None, 'ratings': [], 'reviews': [], 'photos': []}
    id = db['spots'].insert_one(spot_doc)
    return "finished"

def add_rating(rating, review):
    pass

if __name__ == "__main__":
    pass