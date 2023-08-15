# """
# This module takes care of starting the API Server, Loading the DB and Adding the endpoints
# """
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Pesonal Endpoints

## USERS
@app.route("/users", methods=["POST"])
def new_user():
    body = request.json
    email = body.get("email")
    password = body.get("password")
    if email is None or password is None:
        return jsonify({
            "message": "Email and password are required"
        }), 400
    
    user_exist = Users.query.filter_by(email=email).one_or_none()
    if user_exist is not None:
        return jsonify({
            "message": "User already exists"
        }), 400
    user = Users(email, password)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        return jsonify({
            "message": "internal error",
            "error": error.args
        }), 500
    return jsonify({}), 201

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    if id is None: 
        return jsonify({
            "message": "id is required"
        }), 400
    user = Users.query.get(id)
    if user is None:
         return jsonify(""), 404
    return jsonify(user.serialize()), 200

## CHARACTERS

@app.route("/characters", methods=["POST"])
def create_character():
    body = request.json
    type = body.get("type")
    name = body.get("name")
    birth_year = body.get("birth_year")
    gender = body.get("gender")
    hair_color = body.get("hair_color")
    skin_color = body.get("skin_color")
    if type is None or name is None or birth_year is None or gender is None or hair_color is None or skin_color is None:
        return jsonify({
            "message": "all the items are required"
        }), 400
    character = Characters(
        type = type,
        name = name,
        birth_year = birth_year,
        gender = gender,
        hair_color = hair_color,
        skin_color = skin_color
    )
    try:
        db.session.add(character)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        return jsonify({
            "message": "internal error",
            "error": error.args
        }), 500
    return jsonify({}), 201

@app.route("/characters/<int:id>", methods=["GET"])
def get_character(id):
    if id is None: 
        return jsonify({
            "message": "id is required"
        }), 400
    character = Characters.query.get(id)
    if character is None:
         return jsonify(""), 404
    return jsonify(character.serialize()), 200

## PLANETS

@app.route("/planets", methods=["POST"])
def create_planet():
    body = request.json
    type = body.get("type")
    name = body.get("name")
    terrain = body.get("terrain")
    climate = body.get("climate")
    population = body.get("population")
    orbital_period = body.get("orbital_period")
    rotation_period = body.get("rotation_period")
    diameter = body.get("diameter")
    gravity = body.get("gravity")
    surface_water = body.get("surface_water")
    if type is None or name is None or terrain is None or climate is None or population is None or orbital_period is None or rotation_period is None or diameter is None or gravity is None or surface_water is None:
        return jsonify({
            "message": "all the items are required"
        }), 400
    planet = Planets(
        type = type,
        name = name,
        terrain = terrain,
        climate = climate,
        population = population,
        orbital_period = orbital_period,
        rotation_period = rotation_period,
        diameter = diameter,
        gravity = gravity,
        surface_water = surface_water
    )
    try:
        db.session.add(planet)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        return jsonify({
            "message": "internal error",
            "error": error.args
        }), 500
    return jsonify({}), 201

@app.route("/planets/<int:id>", methods=["GET"])
def get_planet(id):
    if id is None: 
        return jsonify({
            "message": "id is required"
        }), 400
    planet = Planets.query.get(id)
    if planet is None:
         return jsonify(""), 404
    return jsonify(planet.serialize()), 200

@app.route("/favorites/users/<int:user_id>", methods=["GET"])
def get_favorites(user_id):
        if user_id is None: 
            return jsonify({
            "message": "id is required"
            }), 400
        favorite = Users.query.get(user_id)
        if favorite is None:
            return jsonify(""), 404
        return jsonify({"favorites" : favorite.serialize()["favorites"]}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
