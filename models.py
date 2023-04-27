from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateBooked = db.Column(db.DateTime(timezone=True), default=func.now())
    dateOfDeparture = db.Column(db.DateTime)
    locationOfDeparture = db.Column(db.String(50))
    locationOfArrival = db.Column(db.String(50))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password= db.Column(db.String(150))
    firstName = db.Column(db.String(30))
    booking = db.relationship('Booking')