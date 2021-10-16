from flask_pymongo import PyMongo
import flask

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def hello_world():
    return "Hello, World!"