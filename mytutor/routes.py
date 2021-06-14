import re
from mytutor.functions import generate_message, generate_json_for_applicants
from mytutor import app, db
from flask import render_template, request
from mytutor.models import Applicants
from sqlalchemy.exc import SQLAlchemyError

db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-all-applicants", methods=['GET'])
def get_all_applicant():
    applicants = Applicants.query.all()
    applicants = map(generate_json_for_applicants, applicants)
    all_applicants = list(applicants)
    return {
        "total_applicants": len(all_applicants),
        "applicants": all_applicants
    }


@app.route("/add-new-applicant", methods=['POST'])
def add_new_applicant():
    try:
        print(request.json)
        name = request.json['name']
        email = request.json['email']
        gender = request.json['gender']
        phone_no = request.json['phone_no']
        country = request.json['country']
        education = request.json['education']
        teaching_experience = request.json['teaching_experience']
        willing_to_teach_courses = request.json['willing_to_teach_courses']
        expected_salary = request.json['expected_salary']
        preferred_currency = request.json['preferred_currency']
        intro = request.json['intro']
        resume = request.json['resume']
        new_applicant = Applicants(name=name, email=email, gender=gender, phone_no=phone_no, country=country, education=education, teaching_experience=teaching_experience,
                                   willing_to_teach_courses=willing_to_teach_courses, expected_salary=expected_salary, preferred_currency=preferred_currency, intro=intro, resume=resume)

        db.session.add(new_applicant)
        db.session.commit()
        return generate_message(200, "application submitted")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(f'{error} fahad aleem 2020')
        if 'already exists'.lower() in error:
            return generate_message(201, "applicant already submitted application")

@app.route("/hire-applicant/<id>", methods=['GET'])
def hire_new_applicant(id):
    return 'hire new applicant'


@app.route("/view-applicant/<id>", methods=['GET'])
def view_applicant_details(id):
    applicant = Applicants.query.get(id)
    if applicant is None:
        return generate_message(201, "Record not found")
    return generate_json_for_applicants(applicant)
