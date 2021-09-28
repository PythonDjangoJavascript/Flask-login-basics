import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()

# Create main App ----->
app = Flask(__name__)

# Creating secreat key for form cerf_token verification ----->
app.config['SECRET_KEY'] = 'MySuperSecretKey'

# Setup Database ----->
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database ----->
db = SQLAlchemy(app)
Migrate(app, db)  # to perform migrations on database and app

# initialize login manager ----->
login_manager.init_app(app)
login_manager.login_view = 'login'  # setting login view
