# Spencer Lommel
# Aug 17th, 2023
# FyneTrack Prototype

import os
from flask import Flask
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from models.models import db, User
from routes.routes import init_routes

# Initialize app and create secret key
app = Flask(__name__)
app.secret_key = os.urandom(16)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fynetrack.db'
db.init_app(app)

# Models go into models folder


# Login Manager
# Should probably be broken out into an extensions.py file
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    init_routes(app)
    app.run(debug=True)
