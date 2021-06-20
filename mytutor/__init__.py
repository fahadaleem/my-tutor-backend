from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fvwllqimerspto:45b6bf19aaf4bddc4ee6614bd759e75e8bb0daad8e7318c0aa6422f97676282c@ec2-35-171-250-21.compute-1.amazonaws.com:5432/dfp3mg7js0oooi'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


from mytutor import routes