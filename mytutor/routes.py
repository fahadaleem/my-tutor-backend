import re
from mytutor.functions import generate_message, generate_json_for_applicants, generate_json_for_teachers
from mytutor import app, db
from flask import render_template, request
from mytutor.models import Applicants, Teachers
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
        if 'UNIQUE constraint failed' in error:
            return generate_message(201, "applicant already submitted application")
        elif 'already exists'.lower() in error:
            return generate_message(201, "applicant already submitted application")


@app.route("/hire-applicant", methods=['POST'])
def hire_new_applicant():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        phone_no = request.json['phone_no']
        gender = request.json['gender']
        country = request.json['country']
        education = request.json['education']
        teaching_experience = request.json['teaching_experience']
        course_code_1 = request.json['course_code_1']
        course_code_2 = request.json['course_code_2']
        salary = request.json['salary']
        preferred_currency = request.json['preferred_currency']
        resume = request.json['resume']
        hiring_date = request.json['hiring_date']
        # add new teacher
        new_Teacher = Teachers(name=name, email=email, password=password, gender=gender, phone_no=phone_no, country=country, education=education, teaching_experience=teaching_experience,
                               course_code_1=course_code_1, course_code_2=course_code_2,  salary=salary, preferred_currency=preferred_currency, resume=resume, hiring_date=hiring_date)
        db.session.add(new_Teacher)
        db.session.commit()
        # delete applicant after hiring
        Applicants.query.filter_by(email=email).delete()
        db.session.commit()
        return generate_message(200, 'Teacher Hired Successfully!')
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        if 'UNIQUE constraint failed' in error:
            return generate_message(201, "This teacher is already hired!")
        elif 'already exists'.lower() in error:
            return generate_message(201, "This teacher is already hired!")


@app.route("/view-applicant/<id>", methods=['GET'])
def view_applicant_details(id):
    applicant = Applicants.query.get(id)
    if applicant is None:
        return generate_message(201, "Record not found")
    return generate_json_for_applicants(applicant)


@app.route("/delete-applicant/<id>", methods=['GET'])
def delete_applicant(id):
    print(id)
    applicant = Applicants.query.filter_by(id=id).delete()
    if applicant == 0:
        return generate_message(201, "Record not found")
    db.session.commit()
    return generate_message(200, "Applicant deleted successfully.")


@app.route("/get-all-teachers", methods=['GET'])
def get_all_teachers():
    all_teachers = list(map(generate_json_for_teachers, Teachers.query.all()))
    return {
        "total_teachers": len(all_teachers),
        "teachers": all_teachers
    }

@app.route("/view-teacher/<id>", methods=['GET'])
def view_teacher(id):
    teacher = Teachers.query.get(id)
    return generate_json_for_teachers(teacher)

@app.route("/delete-teacher/<id>", methods=['GET'])
def delete_teacher(id):
    deleted_teacher = Teachers.query.filter_by(id=id).delete()
    if deleted_teacher == 0:
        return generate_message(201,'No Record Found')
    db.session.commit()
    return generate_message(200, 'Teacher Delete Successfully!')