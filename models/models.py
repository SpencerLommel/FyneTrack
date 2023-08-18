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


