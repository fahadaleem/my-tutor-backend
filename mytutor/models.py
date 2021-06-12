from enum import unique

from flask.sessions import NullSession
from mytutor import db
from datetime import datetime


class Applicants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    education = db.Column(db.String(255), nullable=False)
    teaching_experience = db.Column(db.String(100), nullable=False)
    willing_to_teach_courses = db.Column(db.String(255), nullable=False)
    expected_salary = db.Column(db.Integer, nullable=False)
    preferred_currency = db.Column(db.String(10), nullable=False)
    intro = db.Column(db.Text)
    resume = db.Column(db.String(255), nullable=False)
    applied_on = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'({self.name}, {self.email}, {self.country}, {self.phone_no}, {self.gender}, {self.education}, {self.teaching_experience}, {self.willing_to_teach_courses}, {self.expected_salary}, {self.preferred_currency}, {self.intro}, {self.resume})'


