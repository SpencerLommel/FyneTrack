from flask import render_template, redirect, url_for, flash
from forms.forms import RegisterForm, LoginForm
from models.models import User, db
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash


def init_routes(app):
    @app.route('/test')
    def test_page():
        return '<h1>FyneTrack v0.1.1'

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/login')
    def login():
        login_form = LoginForm()
        return render_template('login.html', form=login_form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        register_form = RegisterForm()
        if register_form.validate_on_submit():
            if db.session.execute(db.select(User).where(User.email == register_form.email.data)).scalar() is None:
                new_user = User(email=register_form.email.data, username=register_form.username.data,
                    password=generate_password_hash(register_form.password.data, method='pbkdf2:sha256', salt_length=8),
                    date_of_birth=register_form.date_of_birth.data)

                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)
                flash("User Successfully Created!")
                return redirect(url_for('home'))
            else:
                flash("Email already associated with account.")
                return redirect(url_for('home'))

        return render_template('register.html', form=register_form)

    @app.route('/app')
    @login_required
    def webapp():
        return render_template('app.html')
