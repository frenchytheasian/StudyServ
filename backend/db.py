import pymongo
from pprint import pprint
from settings import mongo_uri

def get_db():
    uri = mongo_uri()

    client = pymongo.MongoClient(uri)

    db = client['study_spots']

    return db

db = get_db()

def get_study_spots():
    pass

def get_study_spot():
    pass

def add_study_spot(spot_id, name, location, photos):
    """
    Creates a new study spot with the following fields:
    """

    spot_doc = {'spot_id': spot_id, 'name': name, 'location': location, 'avg_rating': None, 'ratings': [], 'reviews': [], 'photos': photos}
    return db['spots'].insert_one(spot_doc)

def add_rating(rating, review):
    pass

if __name__ == "__main__":
    add_study_spot(1, 'Lovejoy Library', 'https://goo.gl/maps/zD79Mvi9XH9MXAPNA', ['photo.jpg', 'image.jpg'])