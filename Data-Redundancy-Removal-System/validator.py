import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()

def validate_data(name, email, phone):

    if not name.strip():
        return False, "Name cannot be empty"

    if not validate_email(email):
        return False, "Invalid Email"

    if not validate_phone(phone):
        return False, "Invalid Phone Number"

    return True, "Valid Data"