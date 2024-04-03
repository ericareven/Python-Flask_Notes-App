from . import db # from website
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func = get today's date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # one(user) to many(notes) relationship: one object(parent) has many children

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func = get today's date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # one(user) to many(journal entries) relationship: one object(parent) has many children

# Add this model to your models.py file
class DailyPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(1000))
    last_used_date = db.Column(db.Date)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # email max length (150 characters) and no two users can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    journal = db.relationship('Journal')

