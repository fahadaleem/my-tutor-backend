from enum import unique
from os import terminal_size

from flask.sessions import NullSession
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
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


class Teachers(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    education = db.Column(db.String(255), nullable=False)
    teaching_experience = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    preferred_currency = db.Column(db.String(10), nullable=False)
    intro = db.Column(db.Text)
    resume = db.Column(db.String(255), nullable=False)
    course_code_1 = db.Column(db.String(50), nullable=True)
    course_code_2 = db.Column(db.String(50), nullable=True)
    hiring_date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'({self.name} {self.email} {self.password} {self.country} {self.phone_no} {self.gender} {self.education} {self.teaching_experience} {self.salary} {self.preferred_currency} {self.intro} {self.course_code_1} {self.course_code_2} {self.resume} {self.hiring_date})'


class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    guardian_name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    CNIC = db.Column(db.String(255), nullable=False, unique = True)
    age = db.Column(db.Integer, nullable=False)
    current_institute = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.full_name} {self.guardian_name} {self.gender} {self.CNIC} {self.age} {self.current_institute} {self.email})'


class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'({self.name} {self.name} {self.email} {self.role})'


class Courses(db.Model):
    __tablename__= "courses"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    course_outline = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)
    visibility = db.Column(db.String(50), nullable=False)
    is_course_assigned = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return f'({self.id} {self.name} {self.description} {self.course_outline} {self.duration} {self.price} {self.language} {self.category} {self.is_course_assigned})'



class Course_Assign(db.Model):
    __tablename__ = 'course_assign'

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id', ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.String(255), db.ForeignKey('courses.id', ondelete="CASCADE"), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.id} {self.course_id} {self.course_id})'


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teachers.id), nullable=False)
    course_id = db.Column(db.String(255), db.ForeignKey(Courses.id), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    reviewer_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'({self.id} {self.comment} {self.teacher_id} {self.course_id} {self.date} {self.reviewer_name})'