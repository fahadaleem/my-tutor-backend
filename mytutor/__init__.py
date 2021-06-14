from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oimevbslxmdpse:eff201d6e4f189b0419cde1cf66e1b1a54af7f99f2ff7e22f3629eb296989482@ec2-35-171-250-21.compute-1.amazonaws.com:5432/dcc47gddmqf9s'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from mytutor import routes