from mytutor import app, db
from flask import render_template
from mytutor.models import Users


db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-all-users")
def get_all_users():
    all_users = Users.query.all()
    return f'{all_users}'
