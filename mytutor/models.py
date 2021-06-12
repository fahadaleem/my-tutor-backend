from enum import unique
from mytutor import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    def __repr__(self):
        return f'({self.id} {self.name} {self.email})'