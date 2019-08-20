from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

login = LoginManager(flask_app)
login.login_view = 'login'

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models

