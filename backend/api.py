
from flask import Flask, jsonify, request
import json

from db import add_study_spot, get_study_spots

app = Flask(__name__)


@app.route('/')
def api_get_study_spots():
    school = app.request.args.get('school')
    search = app.request.args.get('search')

    spots = get_study_spots(school, search)
    response = {
        'spots': spots
    }
    response = json.dumps(response, default=str)
    return jsonify(response)


@app.route('/spots')
def create_spot():
    print(add_study_spot('test', 63121, 'test'))
    return {'test': 'test'}

if __name__ == "__main__":
    app.run()

