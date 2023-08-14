from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='users')

    def __repr__(self):
        return '<Users %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), unique=False, nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)
    climate = db.Column(db.String(250), unique=False, nullable=False)
    population = db.Column(db.String(250), unique=False, nullable=False)
    orbital_period = db.Column(db.String(250), unique=False, nullable=False)
    rotation_period = db.Column(db.String(250), unique=False, nullable=False)
    diameter = db.Column(db.String(250), unique=False, nullable=False)
    gravity = db.Column(db.String(250), unique=False, nullable=False)
    surface_water = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "surface_water": self.surface_water
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), unique=False, nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eyes_color": self.eyes_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_type = db.Column(db.String(250), unique=False, nullable=False)
    item_id = db.Column(db.Integer, unique=False, nullable=False)

