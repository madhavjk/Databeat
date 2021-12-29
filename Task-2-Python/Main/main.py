from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
import requests
from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Place(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key= True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class PlaceUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'place_id', name = 'user_place_unique')


@app.route('/api/places')
def index():
    return jsonify(Place.query.all())

@app.route('/api/places/<int:id>/yes', methods=['POST'])
def yes(id):
    req = requests.get("http://docker.for.win.localhost:8000/api/user")
    json = req.json()

    try:
        placeuser = PlaceUser(user_id=json["id"], place_id = id)
        db.session.add(placeuser)
        db.session.commit()

        publish("place_yes", id)

    except:
        abort(400, "already responded")

    return jsonify({
        "message": "success (yes)"
    })


@app.route('/api/places/<int:id>/no', methods=['POST'])
def no(id):
    req = requests.get("http://docker.for.win.localhost:8000/api/user")
    json = req.json()

    try:
        placeuser = PlaceUser(user_id=json["id"], place_id = id)
        db.session.add(placeuser)
        db.session.commit()

        publish("place_no", id)

    except:
        abort(400, "already responded")

    return jsonify({
        "message": "success (no)"
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0")