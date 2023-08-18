from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    favorites = db.relationship('Favorites', back_populates='users')

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        favorites = [fav.serialize() for fav in self.favorites] 
        return {
            "id": self.id,
            "email": self.email,
            "favorites": favorites
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=True)
    terrain = db.Column(db.String(250), unique=False, nullable=True)
    climate = db.Column(db.String(250), unique=False, nullable=True)
    population = db.Column(db.String(250), unique=False, nullable=True)
    orbital_period = db.Column(db.String(250), unique=False, nullable=True)
    rotation_period = db.Column(db.String(250), unique=False, nullable=True)
    diameter = db.Column(db.String(250), unique=False, nullable=True)
    gravity = db.Column(db.String(250), unique=False, nullable=True)
    surface_water = db.Column(db.String(250), unique=False, nullable=True)
    favorites = db.relationship('Favorites', back_populates='planets')

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
    name = db.Column(db.String(250), unique=False, nullable=True)
    birth_year = db.Column(db.String(250), unique=False, nullable=True)
    gender = db.Column(db.String(250), unique=False, nullable=True)
    hair_color = db.Column(db.String(250), unique=False, nullable=True)
    skin_color = db.Column(db.String(250), unique=False, nullable=True)
    favorites = db.relationship('Favorites', back_populates='characters')

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship("Users", back_populates="favorites")
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    planets = db.relationship("Planets", back_populates="favorites")
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    characters = db.relationship("Characters", back_populates="favorites")

    def serialize(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "planet_id" : self.planet_id,
            "character_id" : self.character_id,
            "user_email" : self.users.email
        }
    
    


