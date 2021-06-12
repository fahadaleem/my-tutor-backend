from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)


app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)

from mytutor import routes