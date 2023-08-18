# Spencer Lommel
# Aug 18th, 2023
# Models file to init DB tables

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model, UserMixin):
    # Required Data
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  # ex '2023-08-17'

    # Optional (For Now)
    # first_name = db.Column(db.String(30), nullable=False)
    # last_name = db.Column(db.String(30), nullable=False)
    # gender = db.Column(db.String(10), nullable=False)
    # profile_picture = db.Column(db.String(100), nullable=False)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_title = db.Column(db.String(50), nullable=False)  # Considering changing to nullable
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)  # Record may not be entered immediately so nullable at start


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    exercise_name = db.Column(db.String(50), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)  # All weights in lb, conversions if needed will be outside DB
    time = db.Column(db.DateTime, nullable=False)  # Time will be used to order when sets are completed within workout




