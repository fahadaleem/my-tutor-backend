import re


def generate_message(code, message):
    return {
        "code":f"{code}",
        "message":f"{message}"
    }

## use for applicants data
def generate_json_for_applicants(data):
    return  {
        "id":f"{data.id}",
        "name":f"{data.name}",
        "email":f"{data.email}",
        "country":f"{data.country}",
        "phone_no":f"{data.phone_no}",
        "gender":f"{data.gender}",
        "education":f"{data.education}",
        "teaching_experience":f"{data.teaching_experience}",
        "willing_to_teach_courses":f"{data.willing_to_teach_courses}",
        "expected_salary":f"{data.expected_salary}",
        "preferred_currency":f"{data.preferred_currency}",
        "intro":f"{data.intro}",
        "resume":f"{data.resume}",
        "applied_date":f"{data.applied_on}"

    }


def generate_json_for_teachers(data):
    return {
        "id":data.id,
        "name":data.name,
        "email":data.email,
        "password":data.password,
        "country":data.country,
        "gender":data.gender,
        "education":data.education,
        "phone_no":data.phone_no,
        "course_code_1":data.course_code_1,
        "course_code_2":data.course_code_2,
        "teaching_experience":data.teaching_experience,
        "salary":data.salary,
        "preferred_currency":data.preferred_currency,
        "resume":data.resume,
        "hiring_date":data.hiring_date
    }


def generate_json_for_students(data):
    return {
        "id":data.id,
        "full_name":data.full_name,
        "guardian_name":data.guardian_name,
        "gender":data.gender,
        "age":data.age,
        "CNIC":data.CNIC,
        "current_institute":data.current_institute,
        "email":data.email
    }

def generate_json_for_admin(data):
    return {
        "id":data.id,
        "name":data.name,
        "email":data.email,
        "password":data.password,
        "role":data.role
    }

def generate_json_for_course(data):
    return {
        "id":data.id,
        "name":data.name, 
        "title":data.title,
        "description":data.description,
        "course_outline":data.course_outline,
        "duration":data.duration,
        "price":data.price,
        "language":data.language,
        "category":data.category,
        "visibility":data.visibility,
        "is_course_assigned":data.is_course_assigned
    }


def generate_json_for_reviews(data):
    return {
        "review_id":data.id,
        "rating":data.rating,
        "comment":data.comment,
        "date":data.date,
        "reviewer_name":data.reviewer_name
    }

def generate_json_for_course_details(data, reviews_info):

    reviews = list(map(generate_json_for_reviews, reviews_info))

    return {
        "teacher_id":data.id,
        "teacher_name":data.teacher_name,
        "teacher_teaching_experience":data.teaching_experience,
        "teacher_gender":data.gender,
        "course_name":data.name,
        "course_title":data.title,
        "course_description":data.description,
        "course_language":data.language,
        "course_category":data.category,
        "course_price":data.price,
        "course_duration":data.duration,
        "course_outline":data.course_outline,
        "total_reviews":len(reviews),
        "reviews":reviews
    }

def generate_json_for_course_details2(data):
    return {
        "id":data.id,
        "course_name":data.name, 
        "course_title":data.title,
        "course_description":data.description,
        "course_outline":data.course_outline,
        "course_duration":data.duration,
        "course_price":data.price,
        "course_language":data.language,
        "course_category":data.category,
        "course_visibility":data.visibility,
        "is_course_assigned":data.is_course_assigned
    }