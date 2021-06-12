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


