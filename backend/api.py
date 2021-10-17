import db
import flask
from flask import Flask, jsonify, request

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)



def get(self):
    return jsonify({'message': 'hello world'})
def post(self):
    data = request.get_json()
    return jsonify({'data': data}), 201



if _name_ == '__main__':
    app.run(debug = True)