from operator import and_
from os import curdir, error
import re
from flask.scaffold import F
from sqlalchemy import exc

from sqlalchemy.orm import eagerload
from sqlalchemy.sql.elements import ReleaseSavepointClause
from mytutor.functions import generate_message, generate_json_for_applicants, generate_json_for_teachers, generate_json_for_students, generate_json_for_admin,generate_json_for_course, generate_json_for_course_details
from mytutor import app, db
from flask import render_template, request
from mytutor.models import Applicants, Teachers, Students, Admin, Courses, Course_Assign, Reviews
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
        return generate_message(201, 'No Record Found')
    db.session.commit()
    return generate_message(200, 'Teacher Delete Successfully!')


@app.route("/add-new-student", methods=['POST'])
def add_new_student():
    try:
        full_name = request.json['full_name']
        guardian_name = request.json['guardian_name']
        gender = request.json['gender']
        CNIC = request.json['CNIC']
        age = request.json['age']
        current_institute = request.json['current_institute']
        email = request.json['email']

        new_student = Students(full_name=full_name, guardian_name=guardian_name, gender=gender,
                               CNIC=CNIC, age=age, current_institute=current_institute, email=email)
        db.session.add(new_student)
        db.session.commit()
        return generate_message(200, "Student acount created succesfully!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        if 'UNIQUE constraint failed' in error:
            return generate_message(201, "Student is already registered")
        elif 'already exists'.lower() in error:
            return generate_message(201, "Student is already registered")


@app.route("/view-student/<id>", methods=['GET'])
def view_student_details(id):
    student = Students.query.get(id)
    if student is None:
        return generate_message(201, "Record not found")
    return generate_json_for_students(student)


@app.route("/get-all-students", methods=['GET'])
def get_all_students():

    if 'email' in request.args:
        email = request.args['email']
        student = Students.query.filter(Students.email == email).first()
        if student is None:
            return generate_message(201, "Record not found")
        return generate_message(200, "Record Found")
    else:
        all_students = Students.query.all()

        all_students = list(map(generate_json_for_students, all_students))
        return {
            "total_students": len(all_students),
            "students": all_students
        }


@app.route("/delete-student/<id>", methods=['GET'])
def delete_student(id):
    student = Students.query.filter_by(id=id).delete()
    if student == 0:
        return generate_message(201, "Record not found")
    db.session.commit()
    return generate_message(200, "Student deleted successfully.")


@app.route("/add-new-admin", methods=['POST'])
def add_new_addmin():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        role = request.json['role']
        new_admin = Admin(name=name, email=email, password=password, role=role)
        db.session.add(new_admin)
        db.session.commit()
        return generate_message(200, "New Admin added successfully!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        if 'UNIQUE constraint failed' in error:
            return generate_message(201, "Admin is already added.")
        elif 'already exists'.lower() in error:
            return generate_message(201, "Admin is already added.")


@app.route("/get-all-admin", methods=['GET'])
def get_all_admin():

    if 'email' in request.args:
        email = request.args['email']
        admin = Admin.query.filter(Admin.email == email).first()
        if admin is None:
            return generate_message(201, "Record not found")
        return {
            "code":"200",
            admin_info:generate_json_for_admin(admin)
        }
    else:
        all_admins = Admin.query.all()
        all_admins = list(map(generate_json_for_admin, all_admins))
        return {
            "total_admins": len(all_admins),
            "admins": all_admins
        }


@app.route("/delete-admin/<id>", methods=['GET'])
def delete_admin(id):
    admin = Admin.query.filter_by(id=id).delete()

    if admin == 0:
        return generate_message(201, 'Record not found')
    db.session.commit()
    return generate_message(200, 'Admin delete successfully!')

@app.route("/add-new-course", methods=['POST'])
def add_new_course():
    try:
        id = request.json['id']
        name = request.json['name']
        title = request.json['title']
        description = request.json['description']
        course_outline = request.json['course_outline']
        duration = request.json['duration']
        price = request.json['price']
        language = request.json['language']
        category = request.json['category']
        visibility = request.json['visibility']

        new_course = Courses(id=id, name=name, description=description, course_outline = course_outline, duration=duration, price=price, language=language, category=category, title=title, visibility=visibility)
        db.session.add(new_course)
        db.session.commit()
        return generate_message(200, "Course added succesfully!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        if 'UNIQUE constraint failed' in error:
            return generate_message(201, "Course is already added.")
        elif 'already exists'.lower() in error:
            return generate_message(201, "Course is already added.")


@app.route("/get-all-courses", methods=['GET'])
def get_all_courses():
    courses = Courses.query.all()
    courses = list(map(generate_json_for_course, courses))
    return {
        "total_courses":len(courses),
        "courses":courses
    }

    
@app.route("/view-course/<id>", methods=['GET'])
def view_course_details(id):
    course = Courses.query.get(str(id).upper())
    if course is None:
        return generate_message(201, "Record not found!")
    return generate_json_for_course(course)


@app.route("/delete-course/<id>", methods=['GET'])
def delete_course(id):
    course = Courses.query.filter_by(id=id).delete()

    if course == 0:
        return generate_message(201,'Record not found!')
    db.session.commit()
    return generate_message(200, "Course deleted successfully!") 


@app.route("/course-assign", methods = ['POST'])
def course_assign():
    teacher_id = request.json['teacher_id']
    course_id = request.json['course_id']
    
    new_course_assign = Course_Assign(teacher_id=teacher_id, course_id=course_id)
    db.session.add(new_course_assign)
    db.session.commit()

    return generate_message(200,'New course assigned successfully!')

@app.route("/add-new-review", methods=['POST'])
def add_new_review():
    rating = request.json['rating']
    comment = request.json['comment']
    teacher_id = request.json['teacher_id']
    course_id = request.json['course_id']
    date = request.json['date']
    reviewer_name = request.json['reviewer_name']

    new_review = Reviews(rating=rating, comment=comment, teacher_id=teacher_id, course_id=course_id, date=date, reviewer_name=reviewer_name)
    db.session.add(new_review)
    db.session.commit()
    return generate_message(200, 'Review added succesfully!')




## localhost:2000/get-all-details?course_id=PY-01&&teacher_id=1
@app.route("/get-course-details", methods=['GET'] )
def get_course_details():
    try:
        course_id = request.args.get('course_id')
        teacher_id = request.args.get('teacher_id')
        course_info = db.session.query(Teachers.id, Teachers.name.label('teacher_name'), Teachers.teaching_experience, Teachers.gender,Courses.name, Courses.title, Courses.description, Courses.price, Courses.course_outline, Courses.duration,Courses.category, Course_Assign).join(Teachers).join(Courses).filter(Courses.id==course_id).one()
        reviews_info = Reviews.query.filter(and_(Reviews.course_id==course_id, Reviews.teacher_id==teacher_id)).all()

        return generate_json_for_course_details(course_info, reviews_info)
    except SQLAlchemyError as e:
        error = str(e)
        return generate_message(201,"Record not found!")


@app.route("/drop-table/<name>")
def drop_table(name):
    db.session.execute(f'drop table {name}')    
    return 'done'


    
@app.route("/show-table/<name>")
def show_table(name):
    results =  db.session.execute(f'select * from {name}').all()    
    return str(results)
