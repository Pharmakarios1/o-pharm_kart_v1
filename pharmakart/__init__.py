from flask import Flask
from pharmakart.tools import generate_uri_from_file
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'd24cea3cd7757ef7e80ca62e1c1a385e'

database_URI = generate_uri_from_file('db_config.yml')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = database_URI

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from pharmakart import routes
