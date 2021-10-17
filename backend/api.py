from flask import Flask, jsonify
import json

from db import add_study_spot, get_study_spots

app = Flask(__name__)


@app.route('/')
def get_home_page():
    spots = get_study_spots(63121)
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